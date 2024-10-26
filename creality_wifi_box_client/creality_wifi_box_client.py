"""Api for the creality wifi box."""

import json

import aiohttp

from .box_info import BoxInfo


class CrealityWifiBoxClient:
    """A client for interacting with the Creality Wifi Box API."""

    _success = 200

    def __init__(self, box_ip: str, box_port: int) -> None:
        """Initialize the CrealityWifiBoxClient with the base URL."""
        self.base_url = f"http://{box_ip}:{box_port}/protocal.csp"

    async def get_info(self) -> BoxInfo:
        """Send a GET request to retrieve device information."""
        url = f"{self.base_url}?fname=Info&opt=main&function=get"
        async with aiohttp.ClientSession() as session, session.get(url) as response:
            response_text = await response.text()
            return BoxInfo.from_dict(json.loads(response_text))

    async def pause_print(self) -> bool:
        """Pause the current print job."""
        url = f"{self.base_url}?fname=net&opt=iot_conf&function=set&pause=1"
        async with aiohttp.ClientSession() as session, session.get(url) as response:
            return response.status == self._success

    async def resume_print(self) -> bool:
        """Resume the current print job."""
        url = f"{self.base_url}?fname=net&opt=iot_conf&function=set&pause=0"
        async with aiohttp.ClientSession() as session, session.get(url) as response:
            return response.status == self._success

    async def stop_print(self) -> bool:
        """Stop the current print job."""
        url = f"{self.base_url}?fname=net&opt=iot_conf&function=set&stop=1"
        async with aiohttp.ClientSession() as session, session.get(url) as response:
            return response.status == self._success
