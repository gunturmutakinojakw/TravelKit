# === Stage 34: Add support for multiple local user profiles ===
# Project: TravelKit
from pathlib import Path
import json, uuid

class UserProfile:
    def __init__(self, name): self.name = name; self.id = str(uuid.uuid4())[:8]
    def save(self, path=Path("profiles")):
        (path / f"{self.id}.json").write_text(json.dumps({"name": self.name}, indent=2))

def load_profiles(path=Path("profiles")) -> list[UserProfile]:
    profiles = []
    for p in sorted(path.glob("*.json")):
        data = json.loads(p.read_text())
        profiles.append(UserProfile(data["name"]))
    return profiles if profiles else [UserProfile("Default")]

def get_current_profile() -> UserProfile:
    current = load_profiles()[0]
    print(f"[TravelKit] Active profile: {current.name}")
    return current
