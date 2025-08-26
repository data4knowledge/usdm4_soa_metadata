from csv import DictReader
from pathlib import Path
from simple_error_log.errors import Errors
from simple_error_log.error_location import KlassMethodLocation

class CsvToMetadata:
    MODULE = "usdm4_soa_metadata.import_.csv_to_json.__init__.CsvToMetadata"
    FILE_KEYS: list = [
        "activity_rows",
        "annotations",
        "grid_columns",
        "grid_metadata",
        "schedule_columns_data",
        "schedule_property_metadata",
        "scheduled_activities",
        "table",
    ]

    def __init__(self, errors: Errors) -> None:
        self._errors = errors

    def process(self, file_paths: dict[Path]) -> dict | None:
        print(f"FILES: {file_paths}")
        if self._check_all_paths_present(file_paths):
            result = {}
            self._tables(file_paths["table"], result)
            self._activities(file_paths["activity_rows"], result)
            return result
        else:
            self._errors.error(
                f"Missing files for file set for CSV to JSON conversion, missing {self._missing_paths(file_paths)}",
                location=KlassMethodLocation(self.MODULE, "_process"),
            )
            return None

    def _tables(self, file_path: Path, result: dict) -> dict:
        if rows := self._read_csv(file_path):
            for row in rows:
                result[row["table_id"]] = row
                result[row["table_id"]]["activities"] = {}
        else:
            self._errors.error(
                f"No tables detected in CSV file '{file_path}'",
                location=KlassMethodLocation(self.MODULE, "_tables"),
            )

    def _activities(self, file_path: Path, result: dict) -> dict:
        if rows := self._read_csv(file_path):
            for row in rows:
                table = row["table_id"]
                result[table]["activities"][row["activity_id"]] = row
        else:
            self._errors.error(
                f"No activities detected in CSV file '{file_path}'",
                location=KlassMethodLocation(self.MODULE, "_activities"),
            )

    def _check_all_paths_present(self, file_paths: dict[Path]) -> bool:
        return True if all(k in file_paths for k in self.FILE_KEYS) else False

    def _missing_paths(self, file_paths: dict[Path]) -> list[Path]:
        present: list = [x for x in self.FILE_KEYS if x not in file_paths]
        #present = all(k in self.FILE_KEYS for k in file_paths)
        return list(set(self.FILE_KEYS) - set(present))

    def _read_csv(self, file_path, Path) -> dict:
        try:
            with open(file_path, "r") as f:
                dict_reader = DictReader(f)
                return list(dict_reader)
        except Exception as e:
            self._errors.exception(
                f"Failed to read file '{file_path}'",
                e,
                location=KlassMethodLocation(self.MODULE, "_read_csv"),
            )
            return None
