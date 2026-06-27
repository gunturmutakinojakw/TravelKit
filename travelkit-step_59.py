# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: TravelKit
from typing import List, Optional
import sys

def bulk_delete_items(items: List[dict], item_type: str, confirm_flag: bool = False) -> int:
    """Delete multiple items of a specific type if confirmation flag is set."""
    deleted_count = 0
    for i in range(len(items)):
        if items[i].get("type") == item_type and (confirm_flag or len(items) <= 1):
            del items[i]
            deleted_count += 1
    return deleted_count

def safe_bulk_remove(trip_data: dict, target_key: str, confirm: bool = False) -> None:
    """Safely remove multiple entries from a trip section with optional confirmation."""
    if not isinstance(trip_data.get(target_key), list):
        return
    
    items_to_delete = [item for item in trip_data[target_key] if "deleted" not in item or not item["deleted"]]
    
    if len(items_to_delete) > 1 and not confirm:
        print(f"[WARN] Found {len(items_to_delete)} items to delete. Set confirm=True to proceed.")
        return

    for item in list(trip_data[target_key]):
        if "type" in item and item["type"] == target_key.replace("_list", "") or target_key.endswith("_list"):
            trip_data[target_key].remove(item)
