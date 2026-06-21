# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: TravelKit
def repair_data_integrity(trip):
    if trip.get("places") and isinstance(trip["places"], list):
        for i, place in enumerate(trip["places"]):
            if "name" not in place:
                place["name"] = f"Unknown Place {i + 1}"
            if "location" not in place:
                place["location"] = ""
    if trip.get("expenses") and isinstance(trip["expenses"], list):
        for i, expense in enumerate(trip["expenses"]):
            if "amount" not in expense or (isinstance(expense["amount"], str) and expense["amount"].strip() == ""):
                expense["amount"] = 0.0
    return trip
