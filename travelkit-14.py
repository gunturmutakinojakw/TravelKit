# === Stage 14: Add file load support with fallback demo data ===
# Project: TravelKit
def load_data(source=None):
    if source:
        try:
            with open(source, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    return {
        "places": [{"id": 1, "name": "Paris", "country": "France"}],
        "packing_list": ["passport", "medication"],
        "expenses": [],
        "day_plans": []
    }
