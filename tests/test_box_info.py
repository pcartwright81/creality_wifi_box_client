"""Tests for the Box Info."""

import unittest
from typing import Any, ClassVar

import pytest

from creality_wifi_box_client.creality_wifi_box_client import BoxInfo


class TestBoxInfo(unittest.TestCase):
    """Test for Box Info."""

    _data: ClassVar[dict[str, Any]] = {
        "opt": "main",
        "fname": "Info",
        "function": "get",
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
        "led_state": 1,
        "error": 0,
    }

    def test_from_dict(self) -> None:  # noqa: C901, PLR0912, PLR0915 Unit testing a massive object.
        """Test creating a BoxInfo object from a dictionary."""
        box_info = BoxInfo.from_dict(self._data)

        if box_info.opt != "main":
            msg = "Incorrect value for 'opt'"
            raise ValueError(msg)
        if box_info.fname != "Info":
            msg = "Incorrect value for 'fname'"
            raise ValueError(msg)
        if box_info.function != "get":
            msg = "Incorrect value for 'function'"
            raise ValueError(msg)
        if box_info.wanmode != "dhcp":
            msg = "Incorrect value for 'wanmode'"
            raise ValueError(msg)
        if box_info.wanphy_link != 1:
            msg = "Incorrect value for 'wanphy_link'"
            raise ValueError(msg)
        if box_info.link_status != 1:
            msg = "Incorrect value for 'link_status'"
            raise ValueError(msg)
        if box_info.wanip != "192.168.1.100":
            msg = "Incorrect value for 'wanip'"
            raise ValueError(msg)
        if box_info.ssid != "MyWiFi":
            msg = "Incorrect value for 'ssid'"
            raise ValueError(msg)
        if box_info.channel != 6:  # noqa: PLR2004
            msg = "Incorrect value for 'channel'"
            raise ValueError(msg)
        if box_info.security != 3:  # noqa: PLR2004
            msg = "Incorrect value for 'security'"
            raise ValueError(msg)
        if box_info.wifipasswd != "password123":
            msg = "Incorrect value for 'wifipasswd'"
            raise ValueError(msg)
        if box_info.apclissid != "MyAP":
            msg = "Incorrect value for 'apclissid'"
            raise ValueError(msg)
        if box_info.apclimac != "12:34:56:78:90:AB":
            msg = "Incorrect value for 'apclimac'"
            raise ValueError(msg)
        if box_info.iot_type != "Creality Cloud":
            msg = "Incorrect value for 'iot_type'"
            raise ValueError(msg)
        if box_info.connect != 1:
            msg = "Incorrect value for 'connect'"
            raise ValueError(msg)
        if box_info.model != "Ender-3":
            msg = "Incorrect value for 'model'"
            raise ValueError(msg)
        if box_info.fan != 0:
            msg = "Incorrect value for 'fan'"
            raise ValueError(msg)
        if box_info.nozzle_temp != 200:  # noqa: PLR2004
            msg = "Incorrect value for 'nozzle_temp'"
            raise ValueError(msg)
        if box_info.bed_temp != 60:  # noqa: PLR2004
            msg = "Incorrect value for 'bed_temp'"
            raise ValueError(msg)
        if box_info.the_1_st_nozzle_temp != 200:  # noqa: PLR2004
            msg = "Incorrect value for 'the_1_st_nozzle_temp'"
            raise ValueError(msg)
        if box_info.the_2_nd_nozzle_temp != 200:  # noqa: PLR2004
            msg = "Incorrect value for 'the_2_nd_nozzle_temp'"
            raise ValueError(msg)
        if box_info.chamber_temp != 40:  # noqa: PLR2004
            msg = "Incorrect value for 'chamber_temp'"
            raise ValueError(msg)
        if box_info.nozzle_temp2 != 200:  # noqa: PLR2004
            msg = "Incorrect value for 'nozzle_temp2'"
            raise ValueError(msg)
        if box_info.bed_temp2 != 60:  # noqa: PLR2004
            msg = "Incorrect value for 'bed_temp2'"
            raise ValueError(msg)
        if box_info.the_1_st_nozzle_temp2 != 200:  # noqa: PLR2004
            msg = "Incorrect value for 'the_1_st_nozzle_temp2'"
            raise ValueError(msg)
        if box_info.the_2_nd_nozzle_temp2 != 200:  # noqa: PLR2004
            msg = "Incorrect value for 'the_2_nd_nozzle_temp2'"
            raise ValueError(msg)
        if box_info.chamber_temp2 != 40:  # noqa: PLR2004
            msg = "Incorrect value for 'chamber_temp2'"
            raise ValueError(msg)
        if box_info.print_name != "Welcome to Creality":
            msg = "Incorrect value for 'print'"
            raise ValueError(msg)
        if box_info.print_progress != 50:  # noqa: PLR2004
            msg = "Incorrect value for 'print_progress'"
            raise ValueError(msg)
        if box_info.stop != 0:
            msg = "Incorrect value for 'stop'"
            raise ValueError(msg)
        if box_info.print_start_time != 1666666666:  # noqa: PLR2004
            msg = "Incorrect value for 'print_start_time'"
            raise ValueError(msg)
        if box_info.state != 1:
            msg = "Incorrect value for 'state'"
            raise ValueError(msg)
        if box_info.err != 0:
            msg = "Incorrect value for 'err'"
            raise ValueError(msg)
        if box_info.box_version != "1.2.3":
            msg = "Incorrect value for 'box_version'"
            raise ValueError(msg)
        if box_info.upgrade != "yes":
            msg = "Incorrect value for 'upgrade'"
            raise ValueError(msg)
        if box_info.upgrade_status != 0:
            msg = "Incorrect value for 'upgrade_status'"
            raise ValueError(msg)
        if box_info.tf_card != 1:
            msg = "Incorrect value for 'tf_card'"
            raise ValueError(msg)
        if box_info.d_progress != 10:  # noqa: PLR2004
            msg = "Incorrect value for 'd_progress'"
            raise ValueError(msg)
        if box_info.layer != 100:  # noqa: PLR2004
            msg = "Incorrect value for 'layer'"
            raise ValueError(msg)
        if box_info.pause != 0:
            msg = "Incorrect value for 'pause'"
            raise ValueError(msg)
        if box_info.reboot != 0:
            msg = "Incorrect value for 'reboot'"
            raise ValueError(msg)
        if box_info.video != 0:
            msg = "Incorrect value for 'video'"
            raise ValueError(msg)
        if box_info.did_string != "abcdefg":
            msg = "Incorrect value for 'did_string'"
            raise ValueError(msg)
        if box_info.api_license != "xyz":
            msg = "Incorrect value for 'api"
            raise ValueError(msg)

    def test_from_dict_missing_field(self) -> None:
        """Test creating a BoxInfo object from a dictionary with a missing field."""
        missing_data = self._data
        del missing_data["fname"]
        with pytest.raises(AssertionError):  # Expect AssertionError for missing field
            BoxInfo.from_dict(missing_data)
