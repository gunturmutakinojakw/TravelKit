# === Stage 20: Add duplicate detection for newly created records ===
# Project: TravelKit
from typing import Optional, List, Dict, Any
import json
import hashlib

def _generate_record_hash(record: Dict[str, Any]) -> str:
    """Generate a unique hash for a record based on its content."""
    # Normalize the record to ensure consistent hashing regardless of key order
    normalized = {k: v for k, v in sorted(record.items()) if isinstance(v, (str, int, float))}
    return hashlib.sha256(json.dumps(normalized, sort_keys=True).encode()).hexdigest()

def check_for_duplicates(new_record: Dict[str, Any], existing_records: List[Dict[str, Any]], 
                         ignore_fields: Optional[List[str]] = None) -> bool:
    """
    Check if a new record is a duplicate of any existing record.
    
    Args:
        new_record: The dictionary representing the new record to check.
        existing_records: A list of dictionaries representing existing records in storage.
        ignore_fields: Optional list of field names to exclude from comparison (e.g., 'id', 'timestamp').
        
    Returns:
        True if a duplicate is found, False otherwise.
    """
    if not new_record or not existing_records:
        return False
        
    # Default fields to ignore for most entities like places and expenses
    default_ignore = {'id', 'created_at', 'updated_at'}
    
    if ignore_fields:
        all_ignored = default_ignore.union(set(ignore_fields))
    else:
        all_ignored = default_ignore
    
    new_hash = _generate_record_hash(new_record)
    
    for existing in existing_records:
        # Skip records that are clearly different by ID if present and not ignored
        if 'id' in existing and 'id' not in all_ignored:
            continue
            
        existing_hash = _generate_record_hash(existing)
        
        if new_hash == existing_hash:
            return True
            
    return False

# Example usage within the main application logic:
# is_duplicate = check_for_duplicates(new_place, stored_places_list)
# if not is_duplicate:
#     stored_places_list.append(new_place)
