# === Stage 64: Add validation for relationship references ===
# Project: TravelKit
def validate_references(data):
    errors = []
    places_set = {p['id'] for p in data.get('places', [])}
    expenses_set = {e['place_id'] for e in data.get('expenses', []) if 'place_id' in e and isinstance(e['place_id'], str)}
    day_plans_set = {dp['place_id'] for dp in data.get('day_plans', []) if 'place_id' in dp and isinstance(dp['place_id'], str)}

    missing_places = expenses_set - places_set
    if missing_places:
        errors.append(f"Expenses reference non-existent places: {missing_places}")

    missing_places_dp = day_plans_set - places_set
    if missing_places_dp:
        errors.append(f"Day plans reference non-existent places: {missing_places_dp}")

    packing_items_place_ids = set()
    for item in data.get('packing_lists', []):
        if isinstance(item, dict) and 'place_id' in item:
            packing_items_place_ids.add(item['place_id'])
    
    missing_places_pack = packing_items_place_ids - places_set
    if missing_places_pack:
        errors.append(f"Packing lists reference non-existent places: {missing_places_pack}")

    return len(errors) == 0, "; ".join(errors)
