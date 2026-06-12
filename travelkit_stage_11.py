# === Stage 11: Add JSON export for the current application state ===
# Project: TravelKit
import json, os

def export_state(travel_data):
    with open("travelkit_export.json", "w", encoding="utf-8") as f:
        json.dump(travel_data, f, indent=2, ensure_ascii=False)
    print(f"State exported to travelkit_export.json ({os.path.getsize('travelkit_export.json')} bytes)")

if __name__ == "__main__":
    export_state(__dict__)
