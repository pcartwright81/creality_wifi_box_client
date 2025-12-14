"""Api for the creality wifi box."""

import json
from types import TracebackType
from typing import Self

import aiohttp

from .box_info import BoxInfo
from .exceptions import (
    ClientConnectionError,
    CommandError,
    InvalidResponseError,
    RequestTimeoutError,
)


class CrealityWifiBoxClient:
    """
    A client for interacting with the Creality Wifi Box API.

    Example:
        async with CrealityWifiBoxClient("192.168.1.100", 8080) as client:
            info = await client.get_info()
            print(f"Printer: {info.model}")
            print(f"Progress: {info.print_progress}%")

            await client.pause_print()

    """

    def __init__(
        self,
        box_ip: str,
        box_port: int,
        timeout: int = 30,
    ) -> None:
        """
        Initialize the CrealityWifiBoxClient with the base URL.

        Args:
            box_ip: IP address of the WiFi Box
            box_port: Port number of the WiFi Box
            timeout: Request timeout in seconds (default: 30)

        """
        self.base_url = f"http://{box_ip}:{box_port}/protocal.csp"
        self._session: aiohttp.ClientSession | None = None
        self._timeout = aiohttp.ClientTimeout(total=timeout)

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create an aiohttp session."""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(timeout=self._timeout)
        return self._session

    async def close(self) -> None:
        """Close the client session and cleanup resources."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    async def __aenter__(self) -> Self:
        """Enter the async context manager."""
        await self._get_session()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the async context manager and cleanup resources."""
        await self.close()

    async def get_info(self) -> BoxInfo:
        """
        Send a GET request to retrieve device information.

        Returns:
            BoxInfo object containing all device information

        Raises:
            ClientConnectionError: If connection to the box fails
            RequestTimeoutError: If the request times out
            InvalidResponseError: If the response is invalid or malformed

        """
        url = f"{self.base_url}?fname=Info&opt=main&function=get"
        try:
            session = await self._get_session()
            async with session.get(url) as response:
                response.raise_for_status()
                response_text = await response.text()
                return BoxInfo.model_validate(json.loads(response_text))
        except aiohttp.ServerTimeoutError as e:
            msg = "Request to WiFi Box timed out"
            raise RequestTimeoutError(msg) from e
        except aiohttp.ClientConnectionError as e:
            msg = f"Failed to connect to WiFi Box: {e}"
            raise ClientConnectionError(msg) from e
        except (json.JSONDecodeError, ValueError) as e:
            msg = f"Invalid response from WiFi Box: {e}"
            raise InvalidResponseError(msg) from e
        except aiohttp.ClientResponseError as e:
            msg = f"HTTP error from WiFi Box: {e.status} {e.message}"
            raise ClientConnectionError(msg) from e

    async def pause_print(self) -> bool:
        """
        Pause the current print job.

        Returns:
            True if successful, False otherwise

        Raises:
            ClientConnectionError: If connection to the box fails
            RequestTimeoutError: If the request times out
            CommandError: If the command fails

        """
        url = f"{self.base_url}?fname=net&opt=iot_conf&function=set&pause=1"
        return await self._send_command(url, "pause print")

    async def resume_print(self) -> bool:
        """
        Resume the current print job.

        Returns:
            True if successful, False otherwise

        Raises:
            ClientConnectionError: If connection to the box fails
            RequestTimeoutError: If the request times out
            CommandError: If the command fails

        """
        url = f"{self.base_url}?fname=net&opt=iot_conf&function=set&pause=0"
        return await self._send_command(url, "resume print")

    async def stop_print(self) -> bool:
        """
        Stop the current print job.

        Returns:
            True if successful, False otherwise

        Raises:
            ClientConnectionError: If connection to the box fails
            RequestTimeoutError: If the request times out
            CommandError: If the command fails

        """
        url = f"{self.base_url}?fname=net&opt=iot_conf&function=set&stop=1"
        return await self._send_command(url, "stop print")

    async def _send_command(self, url: str, command_name: str) -> bool:
        """
        Send a command to the WiFi Box.

        Args:
            url: Full URL for the command
            command_name: Human-readable command name for error messages

        Returns:
            True if successful, False otherwise

        Raises:
            ClientConnectionError: If connection to the box fails
            RequestTimeoutError: If the request times out
            CommandError: If the command fails

        """
        try:
            session = await self._get_session()
            async with session.get(url) as response:
                response.raise_for_status()
                response_text = await response.text()
                success = self.error_message_to_success(response_text)
                if not success:
                    msg = f"Command '{command_name}' failed"
                    raise CommandError(msg)
                return success
        except aiohttp.ServerTimeoutError as e:
            msg = f"Command '{command_name}' timed out"
            raise RequestTimeoutError(msg) from e
        except aiohttp.ClientConnectionError as e:
            msg = f"Failed to connect to WiFi Box: {e}"
            raise ClientConnectionError(msg) from e
        except aiohttp.ClientResponseError as e:
            msg = f"HTTP error for '{command_name}': {e.status} {e.message}"
            raise ClientConnectionError(msg) from e
        except (json.JSONDecodeError, ValueError) as e:
            msg = f"Invalid response for '{command_name}': {e}"
            raise InvalidResponseError(msg) from e

    def error_message_to_success(self, json_string: str) -> bool:
        """
        Get the error status and returns a bool.

        Args:
            json_string: JSON response string from the box

        Returns:
            True if no error (error == 0), False otherwise

        """
        value = json.loads(json_string).get("error")
        return value == 0
