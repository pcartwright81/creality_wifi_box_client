"""Tests for the client."""

import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from creality_wifi_box_client.creality_wifi_box_client import (
    BoxInfo,
    CrealityWifiBoxClient,
)


class TestCrealityWifiBoxClient(unittest.TestCase):
    """Test class for CrealityWifiBoxClient."""

    def setUp(self) -> None:
        """Set up for test methods."""
        self.client = CrealityWifiBoxClient("192.168.1.55", 81)

    @patch("aiohttp.ClientSession.get")
    async def test_get_info(self, mock_get: MagicMock) -> None:
        """Test getting device information."""
        mock_response = AsyncMock()
        mock_response.text = AsyncMock(
            return_value="{"
            '"opt": "main", '
            '"fname": "Info", '
            '"function": "get", '
            '"wanmode": "dhcp", '
            '"wanphy_link": 1, '
            '"link_status": 1, '
            '"wanip": "192.168.1.100", '
            '"ssid": "MyWiFi", '
            '"channel": 6, '
            '"security": 3, '
            '"wifipasswd": "password123", '
            '"apclissid": "MyAP", '
            '"apclimac": "12:34:56:78:90:AB", '
            '"iot_type": "Creality Cloud", '
            '"connect": 1, '
            '"model": "Ender-3", '
            '"fan": 0, '
            '"nozzleTemp": 200, '
            '"bedTemp": 60, '
            '"_1st_nozzleTemp": 200, '
            '"_2nd_nozzleTemp": 200, '
            '"chamberTemp": 40, '
            '"nozzleTemp2": 200, '
            '"bedTemp2": 60, '
            '"_1st_nozzleTemp2": 200, '
            '"_2nd_nozzleTemp2": 200, '
            '"chamberTemp2": 40, '
            '"print": "Welcome to Creality", '
            '"printProgress": 50, '
            '"stop": 0, '
            '"printStartTime": "1666666666", '
            '"state": 1, '
            '"err": 0, '
            '"boxVersion": "1.2.3", '
            '"upgrade": "yes", '
            '"upgradeStatus": 0, '
            '"tfCard": 1, '
            '"dProgress": 10, '
            '"layer": 100, '
            '"pause": 0, '
            '"reboot": 0, '
            '"video": 0, '
            '"DIDString": "abcdefg", '
            '"APILicense": "xyz", '
            '"InitString": "123", '
            '"printedTimes": 10, '
            '"timesLeftToPrint": 90, '
            '"ownerId": "owner123", '
            '"curFeedratePct": 100, '
            '"curPosition": "X10 Y20 Z30", '
            '"autohome": 0, '
            '"repoPlrStatus": 0, '
            '"modelVersion": "4.5.6", '
            '"mcu_is_print": 1, '
            '"printLeftTime": 3600, '
            '"printJobTime": 7200, '
            '"netIP": "192.168.1.101", '
            '"FilamentType": "PLA", '
            '"ConsumablesLen": "1000", '
            '"TotalLayer": 1000, '
            '"led_state": 1, '
            '"error": 0'
            "}"
        )
        mock_get.return_value.__aenter__.return_value = mock_response

        info = await self.client.get_info()

        if not isinstance(info, BoxInfo):
            msg = "Expected BoxInfo object"
            raise TypeError(msg)

    @patch("aiohttp.ClientSession.get")
    async def test_pause_print(self, mock_get: MagicMock) -> None:
        """Test pausing the print job."""
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await self.client.pause_print()
        if not result:
            msg = "Expected pause_print to return True"
            raise ValueError(msg)

    @patch("aiohttp.ClientSession.get")
    async def test_resume_print(self, mock_get: MagicMock) -> None:
        """Test resuming the print job."""
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await self.client.resume_print()
        if not result:
            msg = "Expected resume_print to return True"
            raise ValueError(msg)

    @patch("aiohttp.ClientSession.get")
    async def test_stop_print(self, mock_get: MagicMock) -> None:
        """Test stopping the print job."""
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await self.client.stop_print()
        if not result:
            msg = "Expected stop_print to return True"
            raise ValueError(msg)
