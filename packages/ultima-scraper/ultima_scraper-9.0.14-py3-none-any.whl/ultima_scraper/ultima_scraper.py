import asyncio
import multiprocessing
import threading
import timeit
from contextlib import asynccontextmanager
from ctypes import c_int
from datetime import datetime, timedelta
from multiprocessing.managers import SyncManager
from multiprocessing.sharedctypes import SynchronizedBase
from pathlib import Path
from typing import Any

import ultima_scraper_api
import ultima_scraper_api.helpers.main_helper as main_helper
import ultima_scraper_collection.managers.datascraper_manager.datascrapers.fansly as m_fansly
import ultima_scraper_collection.managers.datascraper_manager.datascrapers.onlyfans as m_onlyfans
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from ultima_scraper_api import SITE_LITERALS, SUPPORTED_SITES
from ultima_scraper_api.apis.onlyfans.classes.auth_model import OnlyFansAuthModel
from ultima_scraper_api.apis.onlyfans.classes.only_drm import OnlyDRM
from ultima_scraper_api.managers.job_manager.jobs.custom_job import CustomJob
from ultima_scraper_collection.config import GlobalAPI, UltimaScraperCollectionConfig
from ultima_scraper_collection.managers.datascraper_manager.datascraper_manager import (
    DataScraperManager,
)
from ultima_scraper_collection.managers.metadata_manager.metadata_manager import (
    MetadataManager,
)
from ultima_scraper_collection.managers.option_manager import OptionManager
from ultima_scraper_collection.managers.server_manager import ServerManager
from ultima_scraper_collection.projects.project_manager import Project
from ultima_scraper_db.databases.ultima_archive import merged_metadata as archive_m
from ultima_scraper_db.databases.ultima_archive.database_api import ArchiveAPI
from ultima_scraper_db.databases.ultima_archive.schemas.templates.site import (
    BoughtContentModel,
    ContentMediaAssoModel,
    JobModel,
    MassMessageModel,
    MassMessageStatModel,
    MessageModel,
    NotificationModel,
    PostModel,
    RemoteURLModel,
    SubscriptionModel,
    UserModel,
)
from ultima_scraper_db.databases.ultima_archive.site_api import SiteAPI
from ultima_scraper_db.managers.database_manager import Alembica

from ultima_scraper.api import App
from ultima_scraper.managers.ui_manager import UiManager

api_types = ultima_scraper_api.api_types
auth_types = ultima_scraper_api.auth_types
user_types = ultima_scraper_api.user_types


class UltimaScraper:
    def __init__(
        self,
        config: UltimaScraperCollectionConfig,
        rest_api: App | None = None,
        process_manager: SyncManager | None = None,
        update_db: bool = False,
    ) -> None:
        self.ui_manager = UiManager()
        self.rest_api = rest_api
        self.option_manager = OptionManager()
        self.config = config
        if process_manager:
            self.active_user = process_manager.Value(c_int, 0)
            self.active_download = process_manager.dict()
            self.misc = process_manager.dict()
        self.update_db = update_db

    async def __aenter__(self):
        await self.init(self.update_db)
        return self

    async def __aexit__(self, exc_type: None, exc_value: None, traceback: None):
        if self.server_manager:
            await self.server_manager.ultima_archive_db_api.management_schema.session.aclose()

            for (
                site_api
            ) in self.server_manager.ultima_archive_db_api.site_apis.values():
                await site_api.schema.session.aclose()

    async def init(self, update_db: bool = False):
        project = Project("UltimaArchiver")

        db_info = self.config.settings.databases[0].connection_info.dict()
        generate = migrate = False
        if update_db:
            generate = migrate = True
        ultima_archive_db = await project._init_db(
            db_info, Alembica(generate=generate, migrate=migrate), archive_m
        )
        self.ultima_archive_db_api = await ArchiveAPI(ultima_archive_db).init()
        self.server_manager = self.ultima_archive_db_api.server_manager
        self.datascraper_manager = DataScraperManager(
            self.ultima_archive_db_api.server_manager, self.config
        )

        # self.ultima_archive_db_api.activate_api(
        #     self.ultima_archive_db_api.fast_api, 2140
        # )

    async def process_server_jobs(
        self,
        site_name: SITE_LITERALS,
        filter_by_user_ids: list[int] = [],
        filter_by_buyer_ids: list[int] = [],
        skip_user_ids: list[int] = [],
    ):
        async with self.ultima_archive_db_api.get_site_api(site_name) as site_db_api:
            downloaded_count = 0
            server_manager = self.server_manager
            server_jobs = await site_db_api.get_jobs(
                server_manager.active_server.id,
                category="download",
                active=True,
                limit=None,
            )

            datascraper = self.datascraper_manager.select_datascraper(
                site_name=site_name
            )

            assert datascraper
            site_db_api.datascraper = datascraper
            for server_job in server_jobs:
                if filter_by_user_ids and server_job.user_id not in filter_by_user_ids:
                    continue
                if skip_user_ids and server_job.user_id in skip_user_ids:
                    continue
                server_job = await self.process_server_job(
                    site_name,
                    server_job,
                    site_db_api,
                    filter_by_buyer_ids=filter_by_buyer_ids,
                )
                if not server_job.active:
                    downloaded_count += 1

    async def process_server_job(
        self,
        site_name: SITE_LITERALS,
        server_job: JobModel,
        site_db_api: SiteAPI,
        filter_by_buyer_ids: list[int] = [],
    ):
        datascraper = site_db_api.datascraper
        assert datascraper
        content_types = datascraper.api.CategorizedContent()
        content_types_keys = content_types.get_keys()
        job_manager = datascraper.api.job_manager
        downloaded_public_content = downloaded_paid_content = False
        db_performer: UserModel | None = None
        async for performer, db_buyer in self.prepared_performer(
            site_name=site_name,
            identifier=server_job.user_id,
            buyer_identifiers=filter_by_buyer_ids,
        ):
            print(
                f"Performer: {performer.username} ({performer.id}) | Authed: {db_buyer.username} ({db_buyer.id})"
            )
            self.active_user.value = performer.id
            if not db_performer:
                db_performer = await site_db_api.get_user(
                    server_job.user_id, load_content=True, load_media=True
                )
                assert db_performer
            authed = performer.get_authed()
            if performer.is_authed_user() and isinstance(authed, OnlyFansAuthModel):
                w9_bytes = await authed.user.get_w9_form()
                if w9_bytes:
                    w9_path = Path(
                        "__user_data__/w9_forms/",
                        f"{authed.user.username} ({authed.user.id}).pdf",
                    )
                    w9_path.parent.mkdir(parents=True, exist_ok=True)
                    w9_path.write_bytes(w9_bytes)

            db_subscription = await db_buyer.find_subscription(db_performer.id)
            metadata_manager = datascraper.find_metadata_manager(db_performer.id)
            content_options = await datascraper.option_manager.create_option(
                content_types_keys, "contents", True
            )
            local_jobs: list[CustomJob] = []
            job_set = job_manager.create_jobs(
                "Scrape",
                ["Messages"],
                datascraper.scrape_vault,
                [performer, db_performer],
            )

            final_content_options = content_options.final_choices
            # downloaded_public_content = True
            if downloaded_public_content:
                removing = ["Stories", "Posts", "Highlights"]
                final_content_options = list(
                    filter(lambda x: x not in removing, final_content_options)
                )
            final_download_options = ["Uncategorized", *final_content_options]

            if not performer.is_authed_user():
                final_download_options.remove("Uncategorized")

            job_set_2 = job_manager.create_jobs(
                "Scrape",
                final_content_options,
                datascraper.prepare_scraper,
                [performer, metadata_manager],
            )
            job_set_3 = job_manager.create_job(
                "DatabaseImport",
                site_db_api.update_user,
                [performer, db_performer],
            )
            job_set_4 = job_manager.create_jobs(
                "Download",
                final_download_options,
                datascraper.prepare_downloads,
                [performer, db_performer],
            )
            local_jobs.extend(job_set + job_set_2 + [job_set_3] + job_set_4)
            performer.jobs.extend(local_jobs)
            for local_job in local_jobs:
                job_manager.queue.put_nowait(local_job)
            await datascraper.datascraper.api.job_manager.process_jobs()
            if all(job.done for job in performer.jobs):
                fmu = datascraper.filesystem_manager.get_file_manager(performer.id)
                await fmu.cleanup()
                downloaded_public_content = downloaded_paid_content = True
            else:
                db_subscription = await db_buyer.find_subscription(db_performer.id)
                if db_subscription:
                    if db_subscription.expires_at > datetime.now().astimezone():
                        downloaded_public_content = True
                        db_subscription.downloaded_at = datetime.now()
                    if db_subscription.paid_content:
                        downloaded_paid_content = True
                else:
                    downloaded_paid_content = True
        if server_job.skippable or downloaded_public_content or downloaded_paid_content:
            server_job.active = False
            server_job.completed_at = datetime.now()
        await site_db_api.get_session().commit()
        return server_job

    async def prepared_performer(
        self,
        site_name: SITE_LITERALS,
        identifier: int | str,
        buyer_identifiers: list[int | str] = [],
    ):
        async with self.ultima_archive_db_api.get_site_api(site_name) as db_site_api:
            db_user = await db_site_api.get_user(identifier)
            if not db_user:
                return
            db_buyers = await db_user.find_buyers(
                active=None if db_user.favorite else True,
                identifiers=buyer_identifiers,
                active_user=True,
            )
            if not db_buyers:
                return

            datascraper = self.datascraper_manager.find_datascraper(site_name)
            assert datascraper
            site_api = datascraper.api
            db_performer = await db_site_api.get_user(identifier, load_aliases=True)
            assert db_performer
            for db_buyer in db_buyers:
                db_auth = db_buyer.find_auth()
                if not db_auth:
                    continue
                auth_details = db_auth.convert_to_auth_details(site_name)
                authed = await site_api.login(auth_details.export())
                if not authed:
                    await db_auth.deactivate()
                    continue
                await db_auth.activate()
                authed.drm = OnlyDRM(
                    Path("__user_data__/drm_device/device_client_id_blob"),
                    Path("__user_data__/drm_device/device_private_key"),
                    authed,
                )
                performer = await datascraper.get_performer(authed, db_performer)
                if not performer:
                    print(
                        f"Performer: {db_performer.username} ({db_performer.id}) not found."
                    )
                    continue
                performer.aliases = [x.username for x in db_performer.aliases]
                await datascraper.prepare_filesystem(performer)
                datascraper.resolve_content_manager(performer)
                yield performer, db_buyer

    async def start(
        self,
        site_name: str,
        api_: api_types | None = None,
    ):
        archive_time = timeit.default_timer()

        datascraper = self.datascraper_manager.select_datascraper(
            site_name,
        )
        if datascraper:
            datascraper.filesystem_manager.activate_directory_manager(
                datascraper.site_config
            )
            await self.start_datascraper(datascraper)
        stop_time = str(int(timeit.default_timer() - archive_time) / 60)[:4]
        await self.ui_manager.display(f"Archive Completed in {stop_time} Minutes")
        return api_

    async def start_datascraper(
        self,
        datascraper: m_onlyfans.OnlyFansDataScraper | m_fansly.FanslyDataScraper,
    ):
        api = datascraper.api
        if datascraper.filesystem_manager.directory_manager:
            datascraper.filesystem_manager.directory_manager.create_directories()
        site_config = datascraper.site_config
        await self.process_profiles(api, self.config.settings)
        scrapable_users: list[user_types] = []
        auth_count = 0
        profile_options = await self.option_manager.create_option(
            api.auths, "profiles", site_config.auto_profile_choice
        )
        api.auths = profile_options.final_choices
        # await dashboard_controller.update_main_table(api)
        identifiers = []
        if site_config.auto_performer_choice:
            subscription_options = await self.option_manager.create_option(
                scrapable_users, "subscriptions", site_config.auto_performer_choice
            )
            if not subscription_options.scrape_all():
                identifiers = subscription_options.return_auto_choice()
            self.option_manager.performer_options = subscription_options
        for auth in api.auths:
            auth: auth_types = auth
            if not auth.get_auth_details():
                continue
            setup = False
            setup, _subscriptions = await datascraper.account_setup(
                auth, site_config, identifiers
            )
            if not setup:
                auth_details: dict[str, Any] = {}
                auth_details["auth"] = auth.get_auth_details().export()
                profiles_directory = datascraper.filesystem_manager.profiles_directory
                _user_auth_filepath = profiles_directory.joinpath(
                    api.site_name, auth.get_auth_details().username, "auth.json"
                )
                # main_helper.export_json(auth_details, user_auth_filepath)
                continue
            auth_count += 1
            scrapable_users.extend(await auth.get_scrapable_users())
            # Do stuff with authed user
            if not auth.drm:
                device_client_id_blob_path = (
                    datascraper.filesystem_manager.devices_directory.joinpath(
                        "device_client_id_blob"
                    )
                )
                device_private_key_path = (
                    datascraper.filesystem_manager.devices_directory.joinpath(
                        "device_private_key"
                    )
                )
                if (
                    device_client_id_blob_path.exists()
                    and device_private_key_path.exists()
                ):
                    auth.drm = OnlyDRM(
                        device_client_id_blob_path,
                        device_private_key_path,
                        auth,
                    )
        await api.remove_invalid_auths()
        subscription_options = await self.option_manager.create_option(
            scrapable_users, "subscriptions", site_config.auto_performer_choice
        )
        self.option_manager.subscription_options = subscription_options
        final_job_user_list = await datascraper.configure_datascraper_jobs()
        await self.assign_jobs(final_job_user_list)
        await datascraper.datascraper.api.job_manager.process_jobs()
        # if global_settings.helpers.delete_empty_directories:
        #     for job_user in job_user_list:
        #         await main_helper.delete_empty_directories(
        #             job_user.directory_manager.user.download_directory,
        #             datascraper.api.filesystem_manager,
        #         )

    async def process_profiles(
        self,
        api: api_types,
        global_settings: UltimaScraperCollectionConfig.Settings,
    ):
        from ultima_scraper_collection.managers.filesystem_manager import (
            FilesystemManager,
        )

        site_name = api.site_name
        filesystem_manager = FilesystemManager()
        profile_directory = filesystem_manager.profiles_directory.joinpath(site_name)
        profile_directory.mkdir(parents=True, exist_ok=True)
        temp_users = list(filter(lambda x: x.is_dir(), profile_directory.iterdir()))
        temp_users = filesystem_manager.remove_mandatory_files(temp_users)
        for user_profile in temp_users:
            user_auth_filepath = user_profile.joinpath("auth.json")
            temp_json_auth = main_helper.import_json(user_auth_filepath)
            json_auth = temp_json_auth.get("auth", {})
            if not json_auth.get("active", None):
                continue
            json_auth["username"] = user_profile.name
            authed = await api.login(json_auth)
            authed.session_manager.add_proxies(global_settings.network.proxies)
            if authed.is_authed():
                site_db_api = self.ultima_archive_db_api.get_site_api(
                    authed.get_api().site_name
                )
                datascraper = (
                    site_db_api.datascraper
                ) = self.datascraper_manager.active_datascraper
                assert datascraper
                await datascraper.filesystem_manager.create_directory_manager(
                    datascraper, authed.user
                )
                found_db_user = await site_db_api.get_user(authed.id)
                await site_db_api.update_user(authed.user, found_db_user)
                pass
            datas = {"auth": authed.get_auth_details().export()}
            if datas:
                main_helper.export_json(datas, user_auth_filepath)
        return api

    async def assign_jobs(self, user_list: set[user_types]):
        datascraper = self.datascraper_manager.active_datascraper
        if not datascraper:
            return
        await self.ui_manager.display("Assigning Jobs")
        filesystem_manager = datascraper.filesystem_manager
        JBM = datascraper.api.job_manager
        site_config = datascraper.site_config
        content_types = datascraper.api.ContentTypes()
        content_types_keys = content_types.get_keys()
        media_types = datascraper.api.MediaTypes()
        media_types_keys = media_types.get_keys()

        for user in user_list:
            await filesystem_manager.create_directory_manager(datascraper, user)
            await filesystem_manager.format_directories(user)
            metadata_manager = MetadataManager(user, filesystem_manager)
            await metadata_manager.process_legacy_metadata()
            datascraper.metadata_manager_users[user.id] = metadata_manager
            authed = user.get_authed()
            site_db = await self.server_manager.get_site_db(
                authed.get_api().site_name, datascraper
            )
            found_db_user = await site_db.get_user(user.id)

            local_jobs: list[CustomJob] = []
            auto_content_choice = (
                site_config.auto_content_choice
                if not user.scrape_whitelist
                else user.scrape_whitelist
            )

            content_options = await self.option_manager.create_option(
                content_types_keys, "contents", auto_content_choice
            )
            jobs = JBM.create_jobs(
                "Scrape",
                content_options.final_choices,
                datascraper.prepare_scraper,
                [user, metadata_manager],
            )
            local_jobs.extend(jobs)

            jobs = JBM.create_job(
                "DatabaseImport",
                site_db.update_user,
                [user, found_db_user],
            )
            local_jobs.append(jobs)

            jobs = JBM.create_jobs(
                "Download",
                content_options.final_choices,
                datascraper.prepare_downloads,
                [user],
            )
            local_jobs.extend(jobs)

            user.jobs.extend(local_jobs)

            media_options = await self.option_manager.create_option(
                media_types_keys, "medias", site_config.auto_media_choice
            )
            JBM.add_media_type_to_jobs(media_options.final_choices)

            for local_job in local_jobs:
                JBM.queue.put_nowait(local_job)
            await asyncio.sleep(0)
        pass
