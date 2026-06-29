# === Stage 67: Add a function that returns key project metrics ===
# Project: TravelKit
def get_project_metrics(trip_data):
    total_places = len(trip_data.get("places", []))
    total_days = len(trip_data.get("day_plans", []))
    total_expenses = sum(item["amount"] for item in trip_data.get("expenses", []) if isinstance(item, dict) and "amount" in item)
    packed_items_count = len(trip_data.get("packing_list", {}).get("items", []))
    planned_days_vs_actual = {day["date"]: day.get("status", "planned") for day in trip_data.get("day_plans", [])}
    return {
        "total_places": total_places,
        "total_days": total_days,
        "total_expenses": round(total_expenses, 2),
        "packed_items_count": packed_items_count,
        "planned_days_vs_actual": planned_days_vs_actual
    }
