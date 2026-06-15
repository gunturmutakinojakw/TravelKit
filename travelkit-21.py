# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: TravelKit
from datetime import datetime, timedelta
import json
from pathlib import Path

def archive_old_records(db_path: str, days_threshold: int = 30):
    """Move records older than threshold to an 'archive' subfolder."""
    db_file = Path(db_path)
    if not db_file.exists(): return
    
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    with open(db_file, "r", encoding="utf-8") as f:
        records = json.load(f)
    
    archived_count = 0
    for record in records:
        if isinstance(record.get("created_at"), str):
            created_dt = datetime.fromisoformat(record["created_at"])
            if created_dt < cutoff_date and not record.get("_archived", False):
                record["_archived"] = True
                archived_count += 1
    
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def restore_archived_records(db_path: str, days_threshold: int = -365):
    """Restore records that were archived within the last threshold (negative means all)."""
    db_file = Path(db_path)
    if not db_file.exists(): return
    
    with open(db_file, "r", encoding="utf-8") as f:
        records = json.load(f)
    
    restored_count = 0
    for record in records:
        if record.get("_archived"):
            created_dt_str = record.get("created_at")
            if isinstance(created_dt_str, str):
                try:
                    created_dt = datetime.fromisoformat(created_dt_str)
                    cutoff_date = datetime.now() + timedelta(days=days_threshold)
                    if created_dt > cutoff_date or days_threshold < 0:
                        record.pop("_archived", None)
                        restored_count += 1
                except ValueError:
                    pass
    
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
