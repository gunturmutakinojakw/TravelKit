# === Stage 35: Add active user switching and user-specific records ===
# Project: TravelKit
from dataclasses import field, asdict
import json
from pathlib import Path
from typing import Optional

class User:
    def __init__(self, name: str):
        self.name = name
        self.records: dict[str, list[dict]] = {}

def load_users() -> list[User]:
    users_path = Path(__file__).parent / "users.json"
    if not users_path.exists():
        return []
    try:
        data = json.loads(users_path.read_text())
        return [User(name=u["name"]) for u in data]
    except Exception:
        return []

def save_users(users: list[User]) -> None:
    Path(__file__).parent.mkdir(parents=True, exist_ok=True)
    users_data = [{"name": u.name} for u in users]
    (Path(__file__).parent / "users.json").write_text(json.dumps(users_data, indent=2))

def get_current_user() -> Optional[User]:
    return load_users()[0] if load_users() else None

def add_record(user: User, category: str, record: dict) -> None:
    user.records.setdefault(category, []).append(record)
    save_users(load_users())
