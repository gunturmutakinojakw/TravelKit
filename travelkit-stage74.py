# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: TravelKit
def compare_snapshots(before: dict, after: dict) -> list[dict]:
    """Generate a diff report between two state snapshots."""
    changes = []
    all_keys = set(before.keys()) | set(after.keys())
    for key in sorted(all_keys):
        b_val = before.get(key)
        a_val = after.get(key)
        if b_val is None:
            changes.append({"type": "added", "key": key, "value": a_val})
        elif a_val is None:
            changes.append({"type": "removed", "key": key, "value": b_val})
        elif type(b_val) != type(a_val):
            changes.append({"type": "changed_type", "key": key, "before": str(type(b_val)), "after": str(type(a_val))})
        else:
            if isinstance(b_val, dict):
                nested_diff = compare_snapshots(b_val, a_val)
                for item in nested_diff:
                    item["parent_key"] = key
                changes.extend(nested_diff)
            elif b_val != a_val:
                changes.append({"type": "changed", "key": key, "before": str(b_val), "after": str(a_val)})
    return changes
