"""Tests for the Creality Wifi Box client."""

from unittest.mock import MagicMock, patch

import pytest

from creality_wifi_box_client.creality_wifi_box_client import (
    BoxInfo,
    CrealityWifiBoxClient,
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

    mock_get.return_value.__aenter__.return_value.text = mock_response

    box_info = await creality_wifi_box_client.get_info()

    assert isinstance(box_info, BoxInfo)
    assert box_info.model == "Ender-3"


@patch("aiohttp.ClientSession.get")
async def test_pause_print(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test pause_print."""

    async def mock_response() -> str:
        return '{"error": 0}'

    mock_get.return_value.__aenter__.return_value.text = mock_response
    success = await creality_wifi_box_client.pause_print()

    assert success is True


@patch("aiohttp.ClientSession.get")
async def test_resume_print(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test resume_print."""

    async def mock_response() -> str:
        return '{"error": 0}'

    mock_get.return_value.__aenter__.return_value.text = mock_response
    success = await creality_wifi_box_client.resume_print()

    assert success is True


@patch("aiohttp.ClientSession.get")
async def test_stop_print(
    mock_get: MagicMock, creality_wifi_box_client: CrealityWifiBoxClient
) -> None:
    """Test stop_print."""

    async def mock_response() -> str:
        return '{"error": 0}'

    mock_get.return_value.__aenter__.return_value.text = mock_response
    success = await creality_wifi_box_client.stop_print()

    assert success is True


async def test_error_message_to_success_true(
    creality_wifi_box_client: CrealityWifiBoxClient,
) -> None:
    """Test error_message_to_bool returns True when error is 0."""
    json_string = '{"error": 0}'
    assert creality_wifi_box_client.error_message_to_success(json_string) is True


async def test_error_message_to_success_false(
    creality_wifi_box_client: CrealityWifiBoxClient,
) -> None:
    """Test error_message_to_bool returns False when error is not 0."""
    json_string = '{"error": 1}'
    assert creality_wifi_box_client.error_message_to_success(json_string) is False
