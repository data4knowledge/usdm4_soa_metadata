from pathlib import Path
from simple_error_log.errors import Errors
from usdm4.api.schedule_timeline import ScheduleTimeline


class UsdmFromJson:
    def __init__(self, errors: Errors) -> None:
        self._errors = errors

    def process(self, file_path: Path) -> list[ScheduleTimeline]:
        pass
