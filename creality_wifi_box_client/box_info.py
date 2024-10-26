"""The info object for the wifi box."""

from typing import Any, TypeVar

T = TypeVar("T")


def _from_str(x: Any) -> str:
    assert isinstance(x, str)  # noqa: S101
    return x


def _from_int(x: Any) -> int:
    assert isinstance(x, int)  # noqa: S101
    assert not isinstance(x, bool)  # noqa: S101
    return x


class BoxInfo:
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
    nozzle_temp: int
    bed_temp: int
    the_1_st_nozzle_temp: int
    the_2_nd_nozzle_temp: int
    chamber_temp: int
    nozzle_temp2: int
    bed_temp2: int
    the_1_st_nozzle_temp2: int
    the_2_nd_nozzle_temp2: int
    chamber_temp2: int
    print: str
    print_progress: int
    stop: int
    print_start_time: int
    state: int
    err: int
    box_version: str
    upgrade: str
    upgrade_status: int
    tf_card: int
    d_progress: int
    layer: int
    pause: int
    reboot: int
    video: int
    did_string: str
    api_license: str
    init_string: str
    printed_times: int
    times_left_to_print: int
    owner_id: str
    cur_feedrate_pct: int
    cur_position: str
    autohome: int
    repo_plr_status: int
    model_version: str
    mcu_is_print: int
    print_left_time: int
    print_job_time: int
    net_ip: str
    filament_type: str
    consumables_len: int
    total_layer: int
    led_state: int
    error: int

    def __init__(  # noqa: PLR0913, PLR0915 Too many statements...Creality.
        self,
        opt: str,
        fname: str,
        function: str,
        wanmode: str,
        wanphy_link: int,
        link_status: int,
        wanip: str,
        ssid: str,
        channel: int,
        security: int,
        wifipasswd: str,
        apclissid: str,
        apclimac: str,
        iot_type: str,
        connect: int,
        model: str,
        fan: int,
        nozzle_temp: int,
        bed_temp: int,
        the_1_st_nozzle_temp: int,
        the_2_nd_nozzle_temp: int,
        chamber_temp: int,
        nozzle_temp2: int,
        bed_temp2: int,
        the_1_st_nozzle_temp2: int,
        the_2_nd_nozzle_temp2: int,
        chamber_temp2: int,
        print_name: str,
        print_progress: int,
        stop: int,
        print_start_time: int,
        state: int,
        err: int,
        box_version: str,
        upgrade: str,
        upgrade_status: int,
        tf_card: int,
        d_progress: int,
        layer: int,
        pause: int,
        reboot: int,
        video: int,
        did_string: str,
        api_license: str,
        init_string: str,
        printed_times: int,
        times_left_to_print: int,
        owner_id: str,
        cur_feedrate_pct: int,
        cur_position: str,
        autohome: int,
        repo_plr_status: int,
        model_version: str,
        mcu_is_print: int,
        print_left_time: int,
        print_job_time: int,
        net_ip: str,
        filament_type: str,
        consumables_len: int,
        total_layer: int,
        led_state: int,
        error: int,
    ) -> None:
        """Initialize a new object."""
        self.opt = opt
        self.fname = fname
        self.function = function
        self.wanmode = wanmode
        self.wanphy_link = wanphy_link
        self.link_status = link_status
        self.wanip = wanip
        self.ssid = ssid
        self.channel = channel
        self.security = security
        self.wifipasswd = wifipasswd
        self.apclissid = apclissid
        self.apclimac = apclimac
        self.iot_type = iot_type
        self.connect = connect
        self.model = model
        self.fan = fan
        self.nozzle_temp = nozzle_temp
        self.bed_temp = bed_temp
        self.the_1_st_nozzle_temp = the_1_st_nozzle_temp
        self.the_2_nd_nozzle_temp = the_2_nd_nozzle_temp
        self.chamber_temp = chamber_temp
        self.nozzle_temp2 = nozzle_temp2
        self.bed_temp2 = bed_temp2
        self.the_1_st_nozzle_temp2 = the_1_st_nozzle_temp2
        self.the_2_nd_nozzle_temp2 = the_2_nd_nozzle_temp2
        self.chamber_temp2 = chamber_temp2
        self.print_name = print_name
        self.print_progress = print_progress
        self.stop = stop
        self.print_start_time = print_start_time
        self.state = state
        self.err = err
        self.box_version = box_version
        self.upgrade = upgrade
        self.upgrade_status = upgrade_status
        self.tf_card = tf_card
        self.d_progress = d_progress
        self.layer = layer
        self.pause = pause
        self.reboot = reboot
        self.video = video
        self.did_string = did_string
        self.api_license = api_license
        self.init_string = init_string
        self.printed_times = printed_times
        self.times_left_to_print = times_left_to_print
        self.owner_id = owner_id
        self.cur_feedrate_pct = cur_feedrate_pct
        self.cur_position = cur_position
        self.autohome = autohome
        self.repo_plr_status = repo_plr_status
        self.model_version = model_version
        self.mcu_is_print = mcu_is_print
        self.print_left_time = print_left_time
        self.print_job_time = print_job_time
        self.net_ip = net_ip
        self.filament_type = filament_type
        self.consumables_len = consumables_len
        self.total_layer = total_layer
        self.led_state = led_state
        self.error = error

    @staticmethod
    def from_dict(obj: Any) -> "BoxInfo":  # noqa: PLR0915 Agree, but not my monkey.
        """Convert to an object from a dictionary."""
        opt = _from_str(obj.get("opt"))
        fname = _from_str(obj.get("fname"))
        function = _from_str(obj.get("function"))
        wanmode = _from_str(obj.get("wanmode"))
        wanphy_link = _from_int(obj.get("wanphy_link"))
        link_status = _from_int(obj.get("link_status"))
        wanip = _from_str(obj.get("wanip"))
        ssid = _from_str(obj.get("ssid"))
        channel = _from_int(obj.get("channel"))
        security = _from_int(obj.get("security"))
        wifipasswd = _from_str(obj.get("wifipasswd"))
        apclissid = _from_str(obj.get("apclissid"))
        apclimac = _from_str(obj.get("apclimac"))
        iot_type = _from_str(obj.get("iot_type"))
        connect = _from_int(obj.get("connect"))
        model = _from_str(obj.get("model"))
        fan = _from_int(obj.get("fan"))
        nozzle_temp = _from_int(obj.get("nozzleTemp"))
        bed_temp = _from_int(obj.get("bedTemp"))
        the_1_st_nozzle_temp = _from_int(obj.get("_1st_nozzleTemp"))
        the_2_nd_nozzle_temp = _from_int(obj.get("_2nd_nozzleTemp"))
        chamber_temp = _from_int(obj.get("chamberTemp"))
        nozzle_temp2 = _from_int(obj.get("nozzleTemp2"))
        bed_temp2 = _from_int(obj.get("bedTemp2"))
        the_1_st_nozzle_temp2 = _from_int(obj.get("_1st_nozzleTemp2"))
        the_2_nd_nozzle_temp2 = _from_int(obj.get("_2nd_nozzleTemp2"))
        chamber_temp2 = _from_int(obj.get("chamberTemp2"))
        print_name = _from_str(obj.get("print"))
        print_progress = _from_int(obj.get("printProgress"))
        stop = _from_int(obj.get("stop"))
        print_start_time = int(_from_str(obj.get("printStartTime")))
        state = _from_int(obj.get("state"))
        err = _from_int(obj.get("err"))
        box_version = _from_str(obj.get("boxVersion"))
        upgrade = _from_str(obj.get("upgrade"))
        upgrade_status = _from_int(obj.get("upgradeStatus"))
        tf_card = _from_int(obj.get("tfCard"))
        d_progress = _from_int(obj.get("dProgress"))
        layer = _from_int(obj.get("layer"))
        pause = _from_int(obj.get("pause"))
        reboot = _from_int(obj.get("reboot"))
        video = _from_int(obj.get("video"))
        did_string = _from_str(obj.get("DIDString"))
        api_license = _from_str(obj.get("APILicense"))
        init_string = _from_str(obj.get("InitString"))
        printed_times = _from_int(obj.get("printedTimes"))
        times_left_to_print = _from_int(obj.get("timesLeftToPrint"))
        owner_id = _from_str(obj.get("ownerId"))
        cur_feedrate_pct = _from_int(obj.get("curFeedratePct"))
        cur_position = _from_str(obj.get("curPosition"))
        autohome = _from_int(obj.get("autohome"))
        repo_plr_status = _from_int(obj.get("repoPlrStatus"))
        model_version = _from_str(obj.get("modelVersion"))
        mcu_is_print = _from_int(obj.get("mcu_is_print"))
        print_left_time = _from_int(obj.get("printLeftTime"))
        print_job_time = _from_int(obj.get("printJobTime"))
        net_ip = _from_str(obj.get("netIP"))
        filament_type = _from_str(obj.get("FilamentType"))
        consumables_len = int(_from_str(obj.get("ConsumablesLen")))
        total_layer = _from_int(obj.get("TotalLayer"))
        led_state = _from_int(obj.get("led_state"))
        error = _from_int(obj.get("error"))
        return BoxInfo(
            opt,
            fname,
            function,
            wanmode,
            wanphy_link,
            link_status,
            wanip,
            ssid,
            channel,
            security,
            wifipasswd,
            apclissid,
            apclimac,
            iot_type,
            connect,
            model,
            fan,
            nozzle_temp,
            bed_temp,
            the_1_st_nozzle_temp,
            the_2_nd_nozzle_temp,
            chamber_temp,
            nozzle_temp2,
            bed_temp2,
            the_1_st_nozzle_temp2,
            the_2_nd_nozzle_temp2,
            chamber_temp2,
            print_name,
            print_progress,
            stop,
            print_start_time,
            state,
            err,
            box_version,
            upgrade,
            upgrade_status,
            tf_card,
            d_progress,
            layer,
            pause,
            reboot,
            video,
            did_string,
            api_license,
            init_string,
            printed_times,
            times_left_to_print,
            owner_id,
            cur_feedrate_pct,
            cur_position,
            autohome,
            repo_plr_status,
            model_version,
            mcu_is_print,
            print_left_time,
            print_job_time,
            net_ip,
            filament_type,
            consumables_len,
            total_layer,
            led_state,
            error,
        )
