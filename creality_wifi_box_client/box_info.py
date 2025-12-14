"""The info object for the wifi box."""

from pydantic import BaseModel, Field, field_validator


class BoxInfo(BaseModel):
    """The class to hold the box information."""

    opt: str
    fname: str
    function: str
    wanmode: str
    wanphy_link: int
    link_status: int
    wanip: str
    ssid: str
    channel: int
    security: int
    wifipasswd: str
    apclissid: str
    apclimac: str
    iot_type: str
    connect: int
    model: str
    fan: int
    nozzle_temp: int = Field(alias="nozzleTemp")
    bed_temp: int = Field(alias="bedTemp")
    the_1_st_nozzle_temp: int = Field(alias="_1st_nozzleTemp")
    the_2_nd_nozzle_temp: int = Field(alias="_2nd_nozzleTemp")
    chamber_temp: int = Field(alias="chamberTemp")
    nozzle_temp2: int = Field(alias="nozzleTemp2")
    bed_temp2: int = Field(alias="bedTemp2")
    the_1_st_nozzle_temp2: int = Field(alias="_1st_nozzleTemp2")
    the_2_nd_nozzle_temp2: int = Field(alias="_2nd_nozzleTemp2")
    chamber_temp2: int = Field(alias="chamberTemp2")
    print_name: str = Field(alias="print")
    print_progress: int = Field(alias="printProgress")
    stop: int
    print_start_time: int = Field(alias="printStartTime")
    state: int
    err: int
    box_version: str = Field(alias="boxVersion")
    upgrade: str
    upgrade_status: int = Field(alias="upgradeStatus")
    tf_card: int = Field(alias="tfCard")
    d_progress: int = Field(alias="dProgress")
    layer: int
    pause: int
    reboot: int
    video: int
    did_string: str = Field(alias="DIDString")
    api_license: str = Field(alias="APILicense")
    init_string: str = Field(alias="InitString")
    printed_times: int = Field(alias="printedTimes")
    times_left_to_print: int = Field(alias="timesLeftToPrint")
    owner_id: str = Field(alias="ownerId")
    cur_feedrate_pct: int = Field(alias="curFeedratePct")
    cur_position: str = Field(alias="curPosition")
    autohome: int
    repo_plr_status: int = Field(alias="repoPlrStatus")
    model_version: str = Field(alias="modelVersion")
    mcu_is_print: int
    print_left_time: int = Field(alias="printLeftTime")
    print_job_time: int = Field(alias="printJobTime")
    net_ip: str = Field(alias="netIP")
    filament_type: str = Field(alias="FilamentType")
    consumables_len: int = Field(alias="ConsumablesLen")
    total_layer: int = Field(alias="TotalLayer")
    led_state: int
    error: bool

    @field_validator(
        "consumables_len",
        "print_start_time",
        mode="before",
    )
    @classmethod
    def parse_empty_string_int(cls, v: str | int) -> int:
        """Handle empty strings for integer fields."""
        if v == "":
            return 0
        return int(v)
