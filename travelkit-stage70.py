# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: TravelKit
from pathlib import Path
import json
from datetime import datetime, timedelta

def clear_state(confirmation: bool) -> None:
    """Clear all trip data after explicit user confirmation."""
    if not confirmation:
        print("⚠️  Operation cancelled. No changes made.")
        return
    
    base_dir = Path(__file__).parent
    files_to_clear = [
        "packing.json",
        "places.json",
        "expenses.json",
        "day_plans.json"
    ]
    
    for filename in files_to_clear:
        filepath = base_dir / filename
        if filepath.exists():
            try:
                content = json.loads(filepath.read_text())
                # Preserve metadata like creation date, clear data
                cleaned_data = {k: v.get("created_at", datetime.now().isoformat()) for k, v in content.items()}
                filepath.write_text(json.dumps(cleaned_data, indent=2))
            except (json.JSONDecodeError, ValueError):
                # If file is corrupted or not JSON, just remove it safely
                if filepath.exists():
                    filepath.unlink()
    
    print("✅ Trip state cleared successfully.")

def confirm_clear_state() -> bool:
    """Prompt user for confirmation to clear data."""
    try:
        response = input("\n⚠️  This will delete all packing lists, places, expenses, and day plans.\n"
                         "Type 'yes' to confirm or press Enter to cancel: ").strip().lower()
        return response == "yes"
    except EOFError:
        print("No input provided. Operation cancelled.")
        return False

if __name__ == "__main__":
    if confirm_clear_state():
        clear_state(True)
