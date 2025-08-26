import yaml


class SheetYamlHelper:
    def __init__(self, yaml_file: str):
        self.yaml_file = yaml_file

    def compare(self, result: dict, save: bool) -> bool:
        if save:
            self._save_yaml(result)
        yaml_data = self._read_yaml()
        return result == yaml_data

    def _save_yaml(self, data: dict) -> None:
        with open(self.yaml_file, "w") as f:
            try:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)
            except Exception as e:
                print(f"EXP. {e}")

    def _read_yaml(self) -> dict:
        with open(self.yaml_file, "r") as f:
            return yaml.safe_load(f)
