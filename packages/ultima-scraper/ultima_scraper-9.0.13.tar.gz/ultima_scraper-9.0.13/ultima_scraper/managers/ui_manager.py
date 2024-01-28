import asyncio
from datetime import datetime
from typing import Any

from websockets import client

from ultima_scraper.managers.dashboard_controller_api import DashboardControllerAPI


class UiManager:
    # Will use this to display things to the terminal in the future
    def __init__(self) -> None:
        self.mode: str = "standard"
        self.dashboard_controller_api: DashboardControllerAPI | None = None

    async def display(self, data: Any, mode: str = ""):
        mode = mode if mode else self.mode
        match mode:
            case "standard":
                print(f"[{datetime.now().replace(microsecond=0)}] {data}")
            case "dashboard":
                if self.dashboard_controller_api:
                    intask = self.dashboard_controller_api.datatable_monitor(data)
                    _task = asyncio.create_task(intask)
                pass
            case _:
                pass

    async def websocket_display(self):
        async with client.connect("ws://localhost:1111/scrape/ws") as websocket:
            while True:
                message = await websocket.recv()
                if isinstance(message, str):
                    print(message)
                elif isinstance(message, dict):
                    print(message.decode())
