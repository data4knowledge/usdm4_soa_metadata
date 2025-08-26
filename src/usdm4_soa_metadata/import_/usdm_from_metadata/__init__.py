from pathlib import Path
from simple_error_log.errors import Errors
from usdm4.api.schedule_timeline import ScheduleTimeline


class UsdmFromMetadata:
    def __init__(self, errors: Errors) -> None:
        self._errors = errors

    def process(self, meatadata: dict) -> list[ScheduleTimeline]:
        pass
