import threading
import mmap
import ctypes
import asyncio
from typing import Callable

from hydrosim_sdk.hydrosim_file import HydroSimFile

from .hydrosim_structs import (
    HydroSimIPC,
    SessionIPC,
    TelemetryIPC,
    TimingIPC,
    CourseInfoIPC,
    BuoysIPC,
)


class HydroSimSDK:
    hydro_sim_file_name = "Local\\HydroSim"
    telemetry_file_name = "Local\\HydroSimTelemetry"
    session_file_name = "Local\\HydroSimSession"
    timing_file_name = "Local\\HydroSimTiming"
    course_info_file_name = "Local\\HydroSimCourseInfo"
    buoys_file_name = "Local\\HydroSimBuoys"

    hydro_sim_file: HydroSimFile = None
    telemetry_file: HydroSimFile = None
    session_file: HydroSimFile = None
    timing_file: HydroSimFile = None
    course_info_file: HydroSimFile = None
    buoys_file: HydroSimFile = None

    running = False

    last_course_info_update = 0

    update_cb: Callable = None
    session_changed_cb: Callable = None

    _last_tick = 0
    _tick_same_count = 0

    def __init__(
        self,
        update_cb: Callable[["HydroSimSDK"], None] = None,
        session_changed_cb: Callable[["HydroSimSDK"], None] = None,
        mmap_name="",
    ):
        self.update_cb = update_cb
        self.session_changed_cb = session_changed_cb

        self.hydro_sim_file: HydroSimFile[HydroSimIPC] = HydroSimFile(
            HydroSimIPC, self.hydro_sim_file_name, mmap_name
        )
        self.telemetry_file: HydroSimFile[TelemetryIPC] = HydroSimFile(
            TelemetryIPC, self.telemetry_file_name, mmap_name
        )
        self.session_file: HydroSimFile[SessionIPC] = HydroSimFile(
            SessionIPC, self.session_file_name, mmap_name
        )
        self.timing_file: HydroSimFile[TimingIPC] = HydroSimFile(
            TimingIPC, self.timing_file_name, mmap_name
        )
        self.course_info_file: HydroSimFile[CourseInfoIPC] = HydroSimFile(
            CourseInfoIPC, self.course_info_file_name, mmap_name
        )
        self.buoys_file: HydroSimFile[BuoysIPC] = HydroSimFile(
            BuoysIPC, self.buoys_file_name, mmap_name
        )

        self.thread = threading.Thread(target=self._start, daemon=True)
        self.thread.start()

    def _start(self):
        asyncio.run(self.update())

    async def update(self):
        while True:
            self.hydro_sim_file.update()
            self.telemetry_file.update()
            self.session_file.update()
            self.timing_file.update()
            self.course_info_file.update()
            self.buoys_file.update()

            if self._last_tick != self.hydro_sim.tick:
                self._tick_same_count = 0
                self.running = True
            else:
                self._tick_same_count += 1
                if self._tick_same_count > 30:
                    self.running = False
                    self.last_course_info_update = 0

            self._last_tick = self.hydro_sim.tick

            if self.session_changed_cb:
                if (
                    self.running
                    and self.last_course_info_update != self.course_info.update
                ):
                    self.last_course_info_update = self.course_info.update
                    self.session_changed_cb(self)

            if self.update_cb:
                self.update_cb(self)

            await asyncio.sleep(0.01666)

    @property
    def hydro_sim(self):
        return self.hydro_sim_file.data

    @property
    def telemetry(self):
        return self.telemetry_file.data

    @property
    def session(self):
        return self.session_file.data

    @property
    def timing(self):
        return self.timing_file.data

    @property
    def course_info(self):
        return self.course_info_file.data

    @property
    def buoys(self):
        return self.buoys_file.data
