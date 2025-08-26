import os
import json
from pathlib import Path
from usdm4_soa_metadata.import_.csv_to_metadata import CsvToMetadata
from simple_error_log.errors import Errors
from tests.usdm4_soa_metadata.helpers.files import read_json, write_json

SAVE = True
ROOT = "tests/usdm4_soa_metadata/test_files/import_/csv_to_metadata/"

def _file_list(directory: Path) -> list[Path]:
    result = {}
    print(f"DIR: {directory}")
    for file in os.listdir(directory):
        print(f"FILE: {file}")
        if file.endswith("activity_rows.csv"):
            result["activities"] = Path(file)
        elif file.endswith("tables.csv"):
            result["tables"] = Path(file)
        else:
            pass
    return result


def _run_test(name: str, save: bool = False):
    file_list = _file_list(Path(os.path.join(ROOT, name)))
    errors = Errors()
    converter = CsvToMetadata(errors)
    result = converter.process(file_list)
    print(f"ERRORS:\n{errors.dump()}")
    pretty_result = json.dumps(result, indent=2)
    result_filename = Path(os.path.join(ROOT, name, "result.json"))
    if save:
        write_json(result_filename, pretty_result)
    expected = read_json(result_filename)
    assert pretty_result == expected


def test_timeline_1():
    _run_test("example_1", SAVE)