"""The info object for the wifi box."""

import unittest
from typing import Any

import pytest

from creality_wifi_box_client.box_info import (
    BoxInfo,
    _from_bool,
    _from_int,
    _from_int_str,
    _from_str,
)


class TestFromStr(unittest.TestCase):
    """Test the _from_str method."""

    def test_valid_input(self) -> None:
        """Test that the method returns the expected value."""
        self.assertEqual(_from_str("test"), "test")

    def test_invalid_input(self) -> None:
        """Test that the method raises a TypeError."""
        with pytest.raises(AssertionError):
            _from_str(123)


class TestFromInt(unittest.TestCase):
    """Test the _from_int method."""

    def test_valid_input(self) -> None:
        """Test that the method returns the expected value."""
        self.assertEqual(_from_int(123), 123)

    def test_bool_input(self) -> None:
        """Test that the method raises a TypeError."""
        with pytest.raises(AssertionError):
            _from_int(True)  # noqa: FBT003

    def test_invalid_input(self) -> None:
        """Test that the method raises a TypeError."""
        with pytest.raises(AssertionError):
            _from_int("test")


class TestFromBool(unittest.TestCase):
    """Test the _from_bool method."""

    def test_true_input(self) -> None:
        """Test that the method returns True for a truthy value."""
        self.assertTrue(_from_bool(1))

    def test_false_input(self) -> None:
        """Test that the method returns False for a falsy value."""
        self.assertFalse(_from_bool(0))

    def test_invalid_input(self) -> None:
        """Test that the method raises a TypeError."""
        with pytest.raises(AssertionError):
            _from_bool("test")


class TestFromIntStr(unittest.TestCase):
    """Test the _from_int_str method."""

    def test_valid_input(self) -> None:
        """Test that the method returns the expected value."""
        self.assertEqual(_from_int_str("123"), 123)

    def test_empty_string(self) -> None:
        """Test that the method returns 0 for an empty string."""
        self.assertEqual(_from_int_str(""), 0)

    def test_invalid_input(self) -> None:
        """Test that the method raises a TypeError."""
        with pytest.raises(AssertionError):
            _from_int_str(123)


class TestBoxInfo(unittest.TestCase):
    """Test the BoxInfo class."""

    def test_from_dict(self) -> None:  # noqa: PLR0915
        """Test creating a BoxInfo object from a dictionary."""
        data: dict[str, Any] = {
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
        box_info = BoxInfo.from_dict(data)

        self.assertEqual(box_info.opt, "main")
        self.assertEqual(box_info.fname, "Info")
        self.assertEqual(box_info.function, "get")
        self.assertEqual(box_info.wanmode, "dhcp")
        self.assertEqual(box_info.wanphy_link, 1)
        self.assertEqual(box_info.link_status, 1)
        self.assertEqual(box_info.wanip, "192.168.1.100")
        self.assertEqual(box_info.ssid, "MyWiFi")
        self.assertEqual(box_info.channel, 6)
        self.assertEqual(box_info.security, 3)
        self.assertEqual(box_info.wifipasswd, "password123")
        self.assertEqual(box_info.apclissid, "MyAP")
        self.assertEqual(box_info.apclimac, "12:34:56:78:90:AB")
        self.assertEqual(box_info.iot_type, "Creality Cloud")
        self.assertEqual(box_info.connect, 1)
        self.assertEqual(box_info.model, "Ender-3")
        self.assertEqual(box_info.fan, 0)
        self.assertEqual(box_info.nozzle_temp, 200)
        self.assertEqual(box_info.bed_temp, 60)
        self.assertEqual(box_info.the_1_st_nozzle_temp, 200)
        self.assertEqual(box_info.the_2_nd_nozzle_temp, 200)
        self.assertEqual(box_info.chamber_temp, 40)
        self.assertEqual(box_info.nozzle_temp2, 200)
        self.assertEqual(box_info.bed_temp2, 60)
        self.assertEqual(box_info.the_1_st_nozzle_temp2, 200)
        self.assertEqual(box_info.the_2_nd_nozzle_temp2, 200)
        self.assertEqual(box_info.chamber_temp2, 40)
        self.assertEqual(box_info.print_name, "Welcome to Creality")
        self.assertEqual(box_info.print_progress, 50)
        self.assertEqual(box_info.stop, 0)
        self.assertEqual(box_info.print_start_time, 1666666666)
        self.assertEqual(box_info.state, 1)
        self.assertEqual(box_info.err, 0)
        self.assertEqual(box_info.box_version, "1.2.3")
        self.assertEqual(box_info.upgrade, "yes")
        self.assertEqual(box_info.upgrade_status, 0)
        self.assertEqual(box_info.tf_card, 1)
        self.assertEqual(box_info.d_progress, 10)
        self.assertEqual(box_info.layer, 100)
        self.assertEqual(box_info.pause, 0)
        self.assertEqual(box_info.reboot, 0)
        self.assertEqual(box_info.video, 0)
        self.assertEqual(box_info.did_string, "abcdefg")
        self.assertEqual(box_info.api_license, "xyz")
        self.assertEqual(box_info.init_string, "123")
        self.assertEqual(box_info.printed_times, 10)
        self.assertEqual(box_info.times_left_to_print, 90)
        self.assertEqual(box_info.owner_id, "owner123")
        self.assertEqual(box_info.cur_feedrate_pct, 100)
        self.assertEqual(box_info.cur_position, "X10 Y20 Z30")
        self.assertEqual(box_info.autohome, 0)
        self.assertEqual(box_info.repo_plr_status, 0)
        self.assertEqual(box_info.model_version, "4.5.6")
        self.assertEqual(box_info.mcu_is_print, 1)
        self.assertEqual(box_info.print_left_time, 3600)
        self.assertEqual(box_info.print_job_time, 7200)
        self.assertEqual(box_info.net_ip, "192.168.1.101")
        self.assertEqual(box_info.filament_type, "PLA")
        self.assertEqual(box_info.consumables_len, 1000)
        self.assertEqual(box_info.total_layer, 1000)
        self.assertEqual(box_info.led_state, 1)
        self.assertEqual(box_info.error, False)
