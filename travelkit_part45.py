# === Stage 45: Add restore from backup with validation ===
# Project: TravelKit
import json, os, hashlib
from pathlib import Path

BACKUP_FILE = "backup.json"
DATA_DIR = Path("data")

def restore_from_backup(backup_path: str) -> bool:
    if not os.path.exists(backup_path):
        print(f"[ERROR] Backup file '{backup_path}' not found.")
        return False
    
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate structure
        required_keys = ["places", "expenses", "packing_list", "day_plans"]
        for key in required_keys:
            if key not in data:
                print(f"[ERROR] Missing required field: {key}")
                return False
        
        # Validate types and nested structures
        if not isinstance(data["places"], list): raise ValueError("Invalid 'places'")
        if not isinstance(data["expenses"], dict): raise ValueError("Invalid 'expenses'")
        if not isinstance(data["packing_list"], list): raise ValueError("Invalid 'packing_list'")
        
        # Validate day_plans structure (list of dicts)
        for plan in data.get("day_plans", []):
            if "date" not in plan or "activities" not in plan:
                print("[ERROR] Invalid format in 'day_plans'.")
                return False
        
        # Restore to disk
        DATA_DIR.mkdir(exist_ok=True)
        
        with open(DATA_DIR / "places.json", 'w') as f: json.dump(data["places"], f, ensure_ascii=False, indent=2)
        with open(DATA_DIR / "expenses.json", 'w') as f: json.dump(data["expenses"], f, ensure_ascii=False, indent=2)
        with open(DATA_DIR / "packing_list.json", 'w') as f: json.dump(data["packing_list"], f, ensure_ascii=False, indent=2)
        
        day_plans = data.get("day_plans", [])
        if day_plans:
            with open(DATA_DIR / "day_plans.json", 'w') as f: json.dump(day_plans, f, ensure_ascii=False, indent=2)
        
        print("[SUCCESS] Backup restored successfully.")
        return True
        
    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON in backup file.")
        return False
    except Exception as e:
        print(f"[ERROR] Restoration failed: {e}")
        return False
