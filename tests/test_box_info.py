"""The info object for the wifi box."""

from typing import Any

import pytest

from creality_wifi_box_client.box_info import BoxInfo


@pytest.fixture
def box_info_data() -> dict[str, Any]:
    """Test data fixture."""
    return {
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


def test_model_validate_network(box_info_data: dict[str, Any]) -> None:
    """Test validating network information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.wanmode == "dhcp"
    assert box_info.wanphy_link == 1
    assert box_info.link_status == 1
    assert box_info.wanip == "192.168.1.100"
    assert box_info.ssid == "MyWiFi"
    assert box_info.channel == 6
    assert box_info.security == 3
    assert box_info.wifipasswd == "password123"
    assert box_info.apclissid == "MyAP"
    assert box_info.apclimac == "12:34:56:78:90:AB"
    assert box_info.iot_type == "Creality Cloud"
    assert box_info.connect == 1
    assert box_info.net_ip == "192.168.1.101"


def test_model_validate_temperatures(box_info_data: dict[str, Any]) -> None:
    """Test validating temperature information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.nozzle_temp == 200
    assert box_info.bed_temp == 60
    assert box_info.the_1_st_nozzle_temp == 200
    assert box_info.the_2_nd_nozzle_temp == 200
    assert box_info.chamber_temp == 40
    assert box_info.nozzle_temp2 == 200
    assert box_info.bed_temp2 == 60
    assert box_info.the_1_st_nozzle_temp2 == 200
    assert box_info.the_2_nd_nozzle_temp2 == 200
    assert box_info.chamber_temp2 == 40


def test_model_validate_print_status(box_info_data: dict[str, Any]) -> None:
    """Test validating print status information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.print_name == "Welcome to Creality"
    assert box_info.print_progress == 50
    assert box_info.stop == 0
    assert box_info.print_start_time == 1666666666
    assert box_info.state == 1
    assert box_info.err == 0
    assert box_info.d_progress == 10
    assert box_info.layer == 100
    assert box_info.pause == 0
    assert box_info.printed_times == 10
    assert box_info.times_left_to_print == 90
    assert box_info.cur_feedrate_pct == 100
    assert box_info.cur_position == "X10 Y20 Z30"
    assert box_info.autohome == 0
    assert box_info.mcu_is_print == 1
    assert box_info.print_left_time == 3600
    assert box_info.print_job_time == 7200
    assert box_info.filament_type == "PLA"
    assert box_info.consumables_len == 1000
    assert box_info.total_layer == 1000


def test_model_validate_device_info(box_info_data: dict[str, Any]) -> None:
    """Test validating device information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.opt == "main"
    assert box_info.fname == "Info"
    assert box_info.function == "get"
    assert box_info.model == "Ender-3"
    assert box_info.fan == 0
    assert box_info.box_version == "1.2.3"
    assert box_info.upgrade == "yes"
    assert box_info.upgrade_status == 0
    assert box_info.tf_card == 1
    assert box_info.reboot == 0
    assert box_info.video == 0
    assert box_info.did_string == "abcdefg"
    assert box_info.api_license == "xyz"
    assert box_info.init_string == "123"
    assert box_info.owner_id == "owner123"
    assert box_info.repo_plr_status == 0
    assert box_info.model_version == "4.5.6"
    assert box_info.led_state == 1
    assert box_info.error is False


def test_consumables_len_empty_string(box_info_data: dict[str, Any]) -> None:
    """Test that an empty string for ConsumablesLen is converted to 0."""
    box_info_data["ConsumablesLen"] = ""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.consumables_len == 0