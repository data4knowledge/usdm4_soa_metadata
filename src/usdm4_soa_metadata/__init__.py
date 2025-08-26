from pathlib import Path
from simple_error_log.errors import Errors
from usdm4.api.schedule_timeline import ScheduleTimeline
from usdm4_soa_metadata.import_.csv_to_metadata import CsvToMetadata
from usdm4_soa_metadata.import_.usdm_from_json import UsdmFromJson
from usdm4_soa_metadata.import_.usdm_from_metadata import UsdmFromMetadata


class USDM4SoAMetadata:
    def __init__(self):
        self._errors = Errors()

    def from_csv(self, file_paths: dict[Path]) -> list[ScheduleTimeline]:
        converter = CsvToJson(self._errors)
        metadata = converter.process(file_paths)
        processor = UsdmFromMetadata(self.errors)
        return processor.process(metadata)

    def from_json(self, file_path: Path) -> list[ScheduleTimeline]:
        processor = UsdmFromJson(self._errors)
        return processor.process(file_path)

    def from_dict(self, metadata: dict) -> list[ScheduleTimeline]:
        processor = UsdmFromMetadata(self._errors)
        return processor.process(metadata)

    @property
    def errors(self) -> Errors:
        return self._errors
