# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: TravelKit
def seed_demo_data(db):
    if db.get("users"): return
    db["users"] = [{"id": 1, "name": "Alex", "email": "alex@example.com"}]
    db["places"] = [
        {"id": 1, "name": "Paris", "country": "France", "notes": "Eiffel Tower"},
        {"id": 2, "name": "Kyoto", "country": "Japan", "notes": "Fushimi Inari Shrine"}
    ]
    db["expenses"] = [
        {"id": 1, "place_id": 1, "amount": 45.00, "category": "food"},
        {"id": 2, "place_id": 2, "amount": 30.00, "category": "transport"}
    ]
    db["packing_list"] = [
        {"item": "Passport", "checked": False},
        {"item": "Sunscreen", "checked": True}
    ]
    db["day_plans"] = [
        {"date": "2024-10-01", "place_id": 1, "activities": ["Visit Louvre", "Seine Cruise"]}
    ]
