# === Stage 46: Add a schema version field and migration helper ===
# Project: TravelKit
SCHEMA_VERSION = "1.0"

def migrate_data(data: dict) -> dict:
    """Apply schema migrations to ensure compatibility with current version."""
    if data.get("schema_version") != SCHEMA_VERSION:
        old_ver = data.get("schema_version", "unknown")
        print(f"Migrating from {old_ver} to {SCHEMA_VERSION}")
        
        # Example migration logic for adding a new field 'notes' with default empty string
        if "notes" not in data and old_ver < SCHEMA_VERSION:
            data["notes"] = ""
            
    return data

def get_schema_version() -> str:
    """Return the current schema version."""
    return SCHEMA_VERSION
