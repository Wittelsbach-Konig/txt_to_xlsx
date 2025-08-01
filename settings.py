import json
from pathlib import Path

SETTINGS_PATH = Path.home() / ".txt_to_xlsx_settings.json"


def get_last_save_path() -> Path:
    """Returns the path to the last saved settings file."""
    if SETTINGS_PATH.exists():
        try:
            data = json.loads(SETTINGS_PATH.read_text())
            return Path(data.get("last_save_path", str(Path.home())))
        except Exception:
            raise FileExistsError("Error while loading settings file")
    return Path.home()


def set_last_save_path(path: Path) -> None:
    """Set the path to the last saved settings file."""
    SETTINGS_PATH.write_text(json.dumps({"last_save_path": str(path)}))
