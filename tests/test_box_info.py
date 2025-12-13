"""The info object for the wifi box."""

from typing import Any

import pytest

from creality_wifi_box_client.box_info import BoxInfo

# Network Constants
TEST_LINK_STATUS_UP = 1
TEST_CHANNEL = 6
TEST_SECURITY_TYPE = 3
TEST_CONNECT_STATUS = 1

# Temperature Constants
TEST_NOZZLE_TEMP = 200
TEST_BED_TEMP = 60
TEST_CHAMBER_TEMP = 40

# Print Status Constants
TEST_PRINT_PROGRESS = 50
TEST_PRINT_START_TIME = 1666666666
TEST_STATE_ACTIVE = 1
TEST_D_PROGRESS = 10
TEST_LAYER = 100
TEST_PRINTED_TIMES = 10
TEST_TIMES_LEFT = 90
TEST_FEEDRATE_PCT = 100
TEST_PRINT_LEFT_TIME = 3600
TEST_PRINT_JOB_TIME = 7200
TEST_CONSUMABLES_LEN = 1000
TEST_TOTAL_LAYER = 1000

# Device Info Constants
TEST_UPGRADE_STATUS = 0
TEST_TF_CARD_PRESENT = 1
TEST_LED_STATE_ON = 1


@pytest.fixture
def box_info_data() -> dict[str, Any]:
    """Test data fixture."""
    return {
        "opt": "main",
        "fname": "Info",
        "function": "get",
        "wanmode": "dhcp",
        "wanphy_link": TEST_LINK_STATUS_UP,
        "link_status": TEST_LINK_STATUS_UP,
        "wanip": "192.168.1.100",
        "ssid": "MyWiFi",
        "channel": TEST_CHANNEL,
        "security": TEST_SECURITY_TYPE,
        "wifipasswd": "password123",
        "apclissid": "MyAP",
        "apclimac": "12:34:56:78:90:AB",
        "iot_type": "Creality Cloud",
        "connect": TEST_CONNECT_STATUS,
        "model": "Ender-3",
        "fan": 0,
        "nozzleTemp": TEST_NOZZLE_TEMP,
        "bedTemp": TEST_BED_TEMP,
        "_1st_nozzleTemp": TEST_NOZZLE_TEMP,
        "_2nd_nozzleTemp": TEST_NOZZLE_TEMP,
        "chamberTemp": TEST_CHAMBER_TEMP,
        "nozzleTemp2": TEST_NOZZLE_TEMP,
        "bedTemp2": TEST_BED_TEMP,
        "_1st_nozzleTemp2": TEST_NOZZLE_TEMP,
        "_2nd_nozzleTemp2": TEST_NOZZLE_TEMP,
        "chamberTemp2": TEST_CHAMBER_TEMP,
        "print": "Welcome to Creality",
        "printProgress": TEST_PRINT_PROGRESS,
        "stop": 0,
        "printStartTime": str(TEST_PRINT_START_TIME),
        "state": TEST_STATE_ACTIVE,
        "err": 0,
        "boxVersion": "1.2.3",
        "upgrade": "yes",
        "upgradeStatus": TEST_UPGRADE_STATUS,
        "tfCard": TEST_TF_CARD_PRESENT,
        "dProgress": TEST_D_PROGRESS,
        "layer": TEST_LAYER,
        "pause": 0,
        "reboot": 0,
        "video": 0,
        "DIDString": "abcdefg",
        "APILicense": "xyz",
        "InitString": "123",
        "printedTimes": TEST_PRINTED_TIMES,
        "timesLeftToPrint": TEST_TIMES_LEFT,
        "ownerId": "owner123",
        "curFeedratePct": TEST_FEEDRATE_PCT,
        "curPosition": "X10 Y20 Z30",
        "autohome": 0,
        "repoPlrStatus": 0,
        "modelVersion": "4.5.6",
        "mcu_is_print": 1,
        "printLeftTime": TEST_PRINT_LEFT_TIME,
        "printJobTime": TEST_PRINT_JOB_TIME,
        "netIP": "192.168.1.101",
        "FilamentType": "PLA",
        "ConsumablesLen": str(TEST_CONSUMABLES_LEN),
        "TotalLayer": TEST_TOTAL_LAYER,
        "led_state": TEST_LED_STATE_ON,
        "error": 0,
    }


def test_model_validate_network(box_info_data: dict[str, Any]) -> None:
    """Test validating network information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.wanmode == "dhcp"
    assert box_info.wanphy_link == TEST_LINK_STATUS_UP
    assert box_info.link_status == TEST_LINK_STATUS_UP
    assert box_info.wanip == "192.168.1.100"
    assert box_info.ssid == "MyWiFi"
    assert box_info.channel == TEST_CHANNEL
    assert box_info.security == TEST_SECURITY_TYPE
    assert box_info.wifipasswd == "password123"
    assert box_info.apclissid == "MyAP"
    assert box_info.apclimac == "12:34:56:78:90:AB"
    assert box_info.iot_type == "Creality Cloud"
    assert box_info.connect == TEST_CONNECT_STATUS
    assert box_info.net_ip == "192.168.1.101"


def test_model_validate_temperatures(box_info_data: dict[str, Any]) -> None:
    """Test validating temperature information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.nozzle_temp == TEST_NOZZLE_TEMP
    assert box_info.bed_temp == TEST_BED_TEMP
    assert box_info.the_1_st_nozzle_temp == TEST_NOZZLE_TEMP
    assert box_info.the_2_nd_nozzle_temp == TEST_NOZZLE_TEMP
    assert box_info.chamber_temp == TEST_CHAMBER_TEMP
    assert box_info.nozzle_temp2 == TEST_NOZZLE_TEMP
    assert box_info.bed_temp2 == TEST_BED_TEMP
    assert box_info.the_1_st_nozzle_temp2 == TEST_NOZZLE_TEMP
    assert box_info.the_2_nd_nozzle_temp2 == TEST_NOZZLE_TEMP
    assert box_info.chamber_temp2 == TEST_CHAMBER_TEMP


def test_model_validate_print_status(box_info_data: dict[str, Any]) -> None:
    """Test validating print status information."""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.print_name == "Welcome to Creality"
    assert box_info.print_progress == TEST_PRINT_PROGRESS
    assert box_info.stop == 0
    assert box_info.print_start_time == TEST_PRINT_START_TIME
    assert box_info.state == TEST_STATE_ACTIVE
    assert box_info.err == 0
    assert box_info.d_progress == TEST_D_PROGRESS
    assert box_info.layer == TEST_LAYER
    assert box_info.pause == 0
    assert box_info.printed_times == TEST_PRINTED_TIMES
    assert box_info.times_left_to_print == TEST_TIMES_LEFT
    assert box_info.cur_feedrate_pct == TEST_FEEDRATE_PCT
    assert box_info.cur_position == "X10 Y20 Z30"
    assert box_info.autohome == 0
    assert box_info.mcu_is_print == 1
    assert box_info.print_left_time == TEST_PRINT_LEFT_TIME
    assert box_info.print_job_time == TEST_PRINT_JOB_TIME
    assert box_info.filament_type == "PLA"
    assert box_info.consumables_len == TEST_CONSUMABLES_LEN
    assert box_info.total_layer == TEST_TOTAL_LAYER


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
    assert box_info.upgrade_status == TEST_UPGRADE_STATUS
    assert box_info.tf_card == TEST_TF_CARD_PRESENT
    assert box_info.reboot == 0
    assert box_info.video == 0
    assert box_info.did_string == "abcdefg"
    assert box_info.api_license == "xyz"
    assert box_info.init_string == "123"
    assert box_info.owner_id == "owner123"
    assert box_info.repo_plr_status == 0
    assert box_info.model_version == "4.5.6"
    assert box_info.led_state == TEST_LED_STATE_ON
    assert box_info.error is False


def test_consumables_len_empty_string(box_info_data: dict[str, Any]) -> None:
    """Test that an empty string for ConsumablesLen is converted to 0."""
    box_info_data["ConsumablesLen"] = ""
    box_info = BoxInfo.model_validate(box_info_data)
    assert box_info.consumables_len == 0
