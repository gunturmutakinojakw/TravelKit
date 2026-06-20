# === Stage 36: Add templates for quickly creating common records ===
# Project: TravelKit
from typing import Dict, List, Optional
import json
from pathlib import Path

class TemplateManager:
    def __init__(self):
        self.templates = {}

    def register(self, name: str, factory) -> None:
        """Register a template factory."""
        self.templates[name] = factory

    def create(self, name: str, **kwargs) -> Optional[Dict]:
        """Create an instance using the registered factory."""
        if name not in self.templates:
            return None
        try:
            return self.templates[name](**kwargs)
        except Exception as e:
            print(f"Error creating template {name}: {e}")
            return None

    def add_place(self, name: str, city: str, country: str, notes: Optional[str] = None) -> Dict:
        """Quickly create a place record."""
        return self.create("place", **{"name": name, "city": city, "country": country, "notes": notes})

    def add_item(self, category: str, item_name: str, quantity: int, unit: str = "pcs") -> Dict:
        """Quickly create a packing list item."""
        return self.create("item", **{"category": category, "name": item_name, "quantity": quantity, "unit": unit})

    def add_expense(self, date: str, description: str, amount: float, currency: str = "USD") -> Dict:
        """Quickly create an expense record."""
        return self.create("expense", **{"date": date, "description": description, "amount": amount, "currency": currency})

    def add_day_plan(self, day_num: int, activities: List[str], notes: Optional[str] = None) -> Dict:
        """Quickly create a day plan."""
        return self.create("day", **{"day": day_num, "activities": activities, "notes": notes})

def _make_place(**data):
    data.setdefault("type", "landmark")
    data.setdefault("status", "planned")
    return {"id": len(data.get("_all_places", [])) + 1, **data}

def _make_item(**data):
    data.setdefault("checked", False)
    return {"id": len(data.get("_all_items", [])) + 1, **data}

def _make_expense(**data):
    data.setdefault("category", "food")
    return {"id": len(data.get("_all_expenses", [])) + 1, **data}

def _make_day(**data):
    data.setdefault("status", "pending")
    return {"id": len(data.get("_all_days", [])) + 1, **data}
