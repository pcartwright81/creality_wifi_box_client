"""Tests for the Creality Wifi Box client."""

from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest

from creality_wifi_box_client.creality_wifi_box_client import (
    BoxInfo,
    CrealityWifiBoxClient,
)
from creality_wifi_box_client.exceptions import (
    CommandError,
    ConnectionError,
    InvalidResponseError,
    TimeoutError,
)

BOX_IP = "192.168.1.100"
BOX_PORT = 8080

# Sample good response from the box
SAMPLE_BOX_INFO_JSON = """
{
    "opt": "main",
    "fname": "Info",
    "function": "get",
    "error": 0,
    "wanmode": "dhcp",
    "wanphy_link": 1,
    "link_status": 1,
    "wanip": "192.168.1.100",
    "ssid": "MyWiFi",
    "channel": 6,
    "security": 3,
    "wifipasswd": "password123",
    "apclissid": "MyAP",
    "apclimac": "12:34:56:78:90:AB",
    "iot_type": "Creality Cloud",
    "connect": 1,
    "model": "Ender-3",
    "fan": 0,
    "nozzleTemp": 200,
    "bedTemp": 60,
    "_1st_nozzleTemp": 200,
    "_2nd_nozzleTemp": 200,
    "chamberTemp": 40,
    "nozzleTemp2": 200,
    "bedTemp2": 60,
    "_1st_nozzleTemp2": 200,
    "_2nd_nozzleTemp2": 200,
    "chamberTemp2": 40,
    "print": "Welcome to Creality",
    "printProgress": 50,
    "stop": 0,
    "printStartTime": "1666666666",
    "state": 1,
    "err": 0,
    "boxVersion": "1.2.3",
    "upgrade": "yes",
    "upgradeStatus": 0,
    "tfCard": 1,
    "dProgress": 10,
    "layer": 100,
    "pause": 0,
    "reboot": 0,
    "video": 0,
    "DIDString": "abcdefg",
    "APILicense": "xyz",
    "InitString": "123",
    "printedTimes": 10,
    "timesLeftToPrint": 90,
    "ownerId": "owner123",
    "curFeedratePct": 100,
    "curPosition": "X10 Y20 Z30",
    "autohome": 0,
    "repoPlrStatus": 0,
    "modelVersion": "4.5.6",
    "mcu_is_print": 1,
    "printLeftTime": 3600,
    "printJobTime": 7200,
    "netIP": "192.168.1.101",
    "FilamentType": "PLA",
    "ConsumablesLen": "1000",
    "TotalLayer": 1000,
    "led_state": 1
}
"""


@pytest.fixture
def creality_wifi_box_client() -> CrealityWifiBoxClient:
    """Creality wifi box client fixture."""
    return CrealityWifiBoxClient(BOX_IP, BOX_PORT)


@patch("aiohttp.ClientSession.get")
async def test_get_info(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test get_info."""

    async def mock_response() -> str:
        return SAMPLE_BOX_INFO_JSON

    mock_response_obj = AsyncMock()
    mock_response_obj.text = mock_response
    mock_response_obj.raise_for_status = MagicMock()
    mock_get.return_value.__aenter__.return_value = mock_response_obj

    box_info = await creality_wifi_box_client.get_info()

    assert isinstance(box_info, BoxInfo)
    assert box_info.model == "Ender-3"
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_pause_print(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test pause_print."""

    async def mock_response() -> str:
        return '{"error": 0}'

    mock_response_obj = AsyncMock()
    mock_response_obj.text = mock_response
    mock_response_obj.raise_for_status = MagicMock()
    mock_get.return_value.__aenter__.return_value = mock_response_obj

    assert await creality_wifi_box_client.pause_print()
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_resume_print(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test resume_print."""

    async def mock_response() -> str:
        return '{"error": 0}'

    mock_response_obj = AsyncMock()
    mock_response_obj.text = mock_response
    mock_response_obj.raise_for_status = MagicMock()
    mock_get.return_value.__aenter__.return_value = mock_response_obj

    assert await creality_wifi_box_client.resume_print()
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_stop_print(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test stop_print."""

    async def mock_response() -> str:
        return '{"error": 0}'

    mock_response_obj = AsyncMock()
    mock_response_obj.text = mock_response
    mock_response_obj.raise_for_status = MagicMock()
    mock_get.return_value.__aenter__.return_value = mock_response_obj

    assert await creality_wifi_box_client.stop_print()
    
    await creality_wifi_box_client.close()


async def test_error_message_to_success_true(
    creality_wifi_box_client: CrealityWifiBoxClient,
) -> None:
    """Test error_message_to_bool returns True when error is 0."""
    json_string = '{"error": 0}'
    assert creality_wifi_box_client.error_message_to_success(json_string)


async def test_error_message_to_success_false(
    creality_wifi_box_client: CrealityWifiBoxClient,
) -> None:
    """Test error_message_to_bool returns False when error is not 0."""
    json_string = '{"error": 1}'
    assert not creality_wifi_box_client.error_message_to_success(json_string)


async def test_context_manager() -> None:
    """Test that the context manager properly closes the session."""
    async with CrealityWifiBoxClient(BOX_IP, BOX_PORT) as client:
        assert client._session is None or not client._session.closed
    
    # After context exit, session should be closed
    assert client._session is None or client._session.closed


async def test_close_idempotent() -> None:
    """Test that close can be called multiple times safely."""
    client = CrealityWifiBoxClient(BOX_IP, BOX_PORT)
    await client.close()
    await client.close()  # Should not raise
    assert client._session is None or client._session.closed


@patch("aiohttp.ClientSession.get")
async def test_connection_error(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test that ConnectionError is raised on connection failure."""
    mock_get.side_effect = aiohttp.ClientConnectionError("Connection failed")
    
    with pytest.raises(ConnectionError, match="Failed to connect"):
        await creality_wifi_box_client.get_info()
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_timeout_error(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test that TimeoutError is raised on timeout."""
    mock_get.side_effect = aiohttp.ServerTimeoutError("Timeout")
    
    with pytest.raises(TimeoutError, match="timed out"):
        await creality_wifi_box_client.get_info()
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_invalid_json_response(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test that InvalidResponseError is raised on invalid JSON."""
    
    async def mock_response() -> str:
        return "not valid json"

    mock_response_obj = AsyncMock()
    mock_response_obj.text = mock_response
    mock_response_obj.raise_for_status = MagicMock()
    mock_get.return_value.__aenter__.return_value = mock_response_obj
    
    with pytest.raises(InvalidResponseError, match="Invalid response"):
        await creality_wifi_box_client.get_info()
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_command_error(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test that CommandError is raised when command fails."""
    
    async def mock_response() -> str:
        return '{"error": 1}'

    mock_response_obj = AsyncMock()
    mock_response_obj.text = mock_response
    mock_response_obj.raise_for_status = MagicMock()
    mock_get.return_value.__aenter__.return_value = mock_response_obj
    
    with pytest.raises(CommandError, match="failed"):
        await creality_wifi_box_client.pause_print()
    
    await creality_wifi_box_client.close()


@patch("aiohttp.ClientSession.get")
async def test_http_error(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test that ConnectionError is raised on HTTP errors."""
    mock_response_obj = AsyncMock()
    mock_response_obj.raise_for_status.side_effect = aiohttp.ClientResponseError(
        request_info=MagicMock(),
        history=(),
        status=500,
        message="Internal Server Error",
    )
    mock_get.return_value.__aenter__.return_value = mock_response_obj
    
    with pytest.raises(ConnectionError, match="HTTP error"):
        await creality_wifi_box_client.get_info()
    
    await creality_wifi_box_client.close()


async def test_custom_timeout() -> None:
    """Test that custom timeout is properly set."""
    client = CrealityWifiBoxClient(BOX_IP, BOX_PORT, timeout=60)
    assert client._timeout.total == 60
    await client.close()
