# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: TravelKit
def _toggle_tag(tags: dict, item_id: str, tag_name: str) -> None:
    if tags.get(item_id):
        tags[item_id].pop(tag_name, None)
    else:
        tags[item_id][tag_name] = True

def _get_tag_summary(items: list[dict], tag_name: str) -> dict[str, int]:
    counts = {}
    for item in items:
        if not isinstance(item.get("tags"), dict): continue
        if item["tags"].get(tag_name):
            cat = item.get("category", "other") or item.get("type", "item")
            counts[cat] = counts.get(cat, 0) + 1
    return counts
