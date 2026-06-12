# === Stage 13: Add file save support using a configurable path ===
# Project: TravelKit
import os
from pathlib import Path

class Config:
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path.home() / ".travelkit"
        self.data_file = self.base_dir / "trip_data.json"
        self.ensure_dirs()

    def ensure_dirs(self):
        self.base_dir.mkdir(parents=True, exist_ok=True)

def save_to_file(data: dict, config: Config) -> None:
    try:
        with open(config.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Failed to save data: {e}")

def load_from_file(config: Config) -> dict:
    if not config.data_file.exists():
        return {}
    try:
        with open(config.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return {}

if __name__ == "__main__":
    cfg = Config()
    print(f"Data will be saved to: {cfg.data_file}")
