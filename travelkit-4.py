# === Stage 4: Implement create operations for the primary records ===
# Project: TravelKit
from datetime import date, timedelta
import random

def create_place(name: str, location: str, description: str = "") -> dict:
    return {
        "id": f"place_{random.randint(1000, 9999)}",
        "name": name,
        "location": location,
        "description": description,
        "created_at": date.today().isoformat()
    }

def create_item(category: str, name: str, quantity: int = 1) -> dict:
    return {
        "id": f"item_{random.randint(1000, 9999)}",
        "category": category,
        "name": name,
        "quantity": quantity,
        "checked": False
    }

def create_expense(date_str: str, amount: float, description: str = "") -> dict:
    return {
        "id": f"expense_{random.randint(1000, 9999)}",
        "date": date_str,
        "amount": amount,
        "description": description
    }

def create_day_plan(day_num: int, activities: list) -> dict:
    return {
        "id": f"day_{day_num}",
        "day_number": day_num,
        "activities": activities,
        "notes": ""
    }
