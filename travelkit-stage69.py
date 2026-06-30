# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: TravelKit
import json, os, random, string
from pathlib import Path

def reset_demo_data():
    base = Path(__file__).parent / "data"
    places_file = base / "places.json"
    expenses_file = base / "expenses.json"
    
    if not places_file.exists() or not expenses_file.exists():
        print("Error: data files missing.")
        return
    
    with open(places_file) as f:
        places = json.load(f)
    with open(expenses_file) as f:
        expenses = json.load(f)
    
    demo_places = [
        {"id": 1, "name": "Paris", "country": "France", "notes": "Eiffel Tower"},
        {"id": 2, "name": "Kyoto", "country": "Japan", "notes": "Fushimi Inari"},
    ]
    
    demo_expenses = [
        {"id": 101, "place_id": 1, "amount": 45.50, "category": "food", "date": "2023-10-01"},
        {"id": 102, "place_id": 1, "amount": 120.00, "category": "transport", "date": "2023-10-02"},
    ]
    
    for p in demo_places:
        existing = next((x for x in places if x["id"] == p["id"]), None)
        if not existing:
            places.append(p)
            
    for e in demo_expenses:
        existing = next((x for x in expenses if x["id"] == e["id"]), None)
        if not existing:
            expenses.append(e)
    
    random.seed(42)
    suffix = "".join(random.choices(string.ascii_lowercase, k=8))
    
    with open(places_file, "w") as f:
        json.dump({"version": 1, "demo_suffix": suffix, "data": places}, f, indent=2)
        
    with open(expenses_file, "w") as f:
        json.dump({"version": 1, "demo_suffix": suffix, "data": expenses}, f, indent=2)
        
    print(f"Demo data reset successfully. Suffix: {suffix}")
