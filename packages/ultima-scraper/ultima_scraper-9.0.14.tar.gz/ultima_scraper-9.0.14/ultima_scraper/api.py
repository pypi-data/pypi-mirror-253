from multiprocessing import Process
from typing import TYPE_CHECKING, Any

import requests
import uvicorn
from fastapi import (
    APIRouter,
    Depends,
    FastAPI,
    HTTPException,
    Request,
    Response,
    WebSocket,
)
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

if TYPE_CHECKING:
    from ultima_scraper.ultima_scraper import UltimaScraper


def p_function(fast_api: FastAPI, port: int):
    uvicorn.run(  # type: ignore
        fast_api,
        host="0.0.0.0",
        port=port,
        # log_level="debug",
    )


def activate_api(fast_api: FastAPI, port: int):
    origins = [
        "*",
    ]
    fast_api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server = Process(
        target=p_function,
        args=(
            fast_api,
            port,
        ),
        daemon=True,
    )
    server.start()
    while True:
        try:
            requests.get(f"http://localhost:{port}")
            break
        except requests.exceptions.ConnectionError:
            continue
    return server


class App(FastAPI):
    ultima_scraper: "UltimaScraper"

    def __init__(
        self,
        ultima_scraper: "UltimaScraper",
        *args: tuple[Any],
        **kwargs: dict[str, Any],
    ):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.ultima_scraper = ultima_scraper
        App.ultima_scraper = ultima_scraper
        self.include_router(router)


router = APIRouter(
    prefix="/scrape",
    responses={404: {"description": "Not found"}},
)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text(f"Message text was: {'data'}")


class ScrapeAndDownloadOptions(BaseModel):
    authed_identifiers: list[int | str] = []
    site_name: str
    username: str


@router.get("/")
async def root(options: ScrapeAndDownloadOptions):
    ultima_scraper = App.ultima_scraper
    site_name = options.site_name
    async with ultima_scraper.ultima_archive_db_api.get_site_api(
        site_name
    ) as db_site_api:
        performer = await ultima_scraper.prepared_performer(
            site_name=site_name,
            identifier=options.username,
            buyer_identifiers=options.authed_identifiers,
        )
        if performer:
            db_performer = await db_site_api.get_user(performer.id, load_content=True)
            datascraper = ultima_scraper.datascraper_manager.find_datascraper(site_name)
            assert datascraper
            db_site_api.datascraper = datascraper
            metadata_manager = await ultima_scraper.prepare_filesystem(performer)
            api = performer.get_api()
            job_manager = api.job_manager
            local_jobs: list[Any] = []
            jobs = job_manager.create_jobs(
                "Scrape",
                # content_options.final_choices,
                ["Posts"],
                datascraper.prepare_scraper,
                [performer, metadata_manager],
            )
            local_jobs.extend(jobs)
            jobs = job_manager.create_job(
                "DatabaseImport",
                db_site_api.update_user,
                [performer, db_performer],
            )
            local_jobs.extend([jobs])
            performer.jobs.extend(local_jobs)
            for local_job in local_jobs:
                job_manager.queue.put_nowait(local_job)
            await job_manager.process_jobs()
        else:
            return {"status": False}
        return {"status": True}


@router.get("/download")
async def download(options: ScrapeAndDownloadOptions):
    ultima_scraper = App.ultima_scraper
    site_name = options.site_name
    datascraper = ultima_scraper.datascraper_manager.find_datascraper(site_name)
    assert datascraper
    performers = datascraper.api.find_user(options.username)
    for performer in performers:
        api = performer.get_api()
        job_manager = api.job_manager
        jobs = job_manager.create_jobs(
            "Download",
            # content_options.final_choices,
            ["Posts"],
            datascraper.prepare_downloads,
            [performer],
        )
        job_manager.queue.put_nowait(jobs[0])
        performer.jobs.extend(jobs)
        await job_manager.process_jobs()
    return {"status": True}


@router.get("/active_user")
async def active_user():
    ultima_scraper = App.ultima_scraper
    active_user_value = ultima_scraper.active_user.value
    final_value = active_user_value if active_user_value != 0 else None
    return {"active_user": final_value}
