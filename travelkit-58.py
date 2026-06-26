# === Stage 58: Add bulk update behavior for selected records ===
# Project: TravelKit
def bulk_update_records(records: list, updates: dict) -> int:
    """Apply a single update field to all provided records and return count of modified items."""
    if not records or not updates:
        return 0
    
    updated_count = 0
    for record in records:
        try:
            # Safely apply each key-value pair from the updates dictionary
            for key, value in updates.items():
                if hasattr(record, key):
                    setattr(record, key, value)
                    updated_count += 1
        except Exception as e:
            print(f"Failed to update record {record}: {e}")
    
    return updated_count
