# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: TravelKit
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List, Dict, Any

@dataclass
class Place:
    name: str
    category: str
    description: str = ""
    coordinates: Optional[Dict[str, float]] = None
    tags: List[str] = field(default_factory=list)

@dataclass
class Expense:
    date: date
    amount: float
    category: str
    description: str = ""
    receipt_url: Optional[str] = None

@dataclass
class PackingItem:
    name: str
    quantity: int = 1
    category: str = "general"
    packed: bool = False
    notes: str = ""

@dataclass
class DayPlan:
    date: date
    theme: str = ""
    places: List[Place] = field(default_factory=list)
    activities: List[str] = field(default_factory=list)
    budget: float = 0.0

def create_sample_data() -> Dict[str, Any]:
    sample_place = Place(
        name="Central Park",
        category="park",
        description="Large urban park with walking trails.",
        tags=["nature", "relax"]
    )
    
    sample_expense = Expense(
        date=date.today(),
        amount=15.50,
        category="food",
        description="Lunch at local cafe"
    )
    
    sample_item = PackingItem(
        name="Passport",
        quantity=1,
        category="documents",
        packed=True
    )
    
    sample_day_plan = DayPlan(
        date=date.today(),
        theme="City Tour",
        places=[sample_place],
        activities=["Walk in park", "Visit museum"],
        budget=50.0
    )
    
    return {
        "places": [sample_place],
        "expenses": [sample_expense],
        "packing_list": [sample_item],
        "day_plans": [sample_day_plan]
    }
