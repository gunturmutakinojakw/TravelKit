# === Stage 63: Add relationships between records where useful ===
# Project: TravelKit
from typing import Optional, Dict, List
import json
from pathlib import Path

class TravelKitDB:
    def __init__(self):
        self.data = {}
    
    def load(self, path: str) -> None:
        with open(path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    def save(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

def link_records(db: TravelKitDB, day_id: str, place_ids: List[str], expense_ids: Optional[List[str]] = None) -> None:
    if 'days' not in db.data or 'places' not in db.data or 'expenses' not in db.data:
        return
    
    day = db.data['days'].get(day_id)
    if not day:
        return
    
    day.setdefault('linked_places', []).extend(place_ids)
    
    if expense_ids:
        day.setdefault('linked_expenses', []).extend(expense_ids)

def create_trip_plan(db: TravelKitDB, trip_name: str, days_data: List[Dict], places_data: List[Dict]) -> None:
    db.data['trip'] = {
        'name': trip_name,
        'days': [d for d in days_data if isinstance(d, dict)],
        'places': [p for p in places_data if isinstance(p, dict)]
    }

def add_relationships(db: TravelKitDB) -> None:
    # Link each day to its associated places and expenses
    for day_id, day_info in db.data.get('days', {}).items():
        linked_places = [p['id'] for p in db.data.get('places', []) if p.get('day') == int(day_id)]
        linked_expenses = []
        
        # Link expenses to the specific day they occurred on
        for expense_info in db.data.get('expenses', {}).values():
            exp_day = expense_info.get('date') or 0
            if exp_day and str(exp_day) == day_id:
                linked_expenses.append(expense_info['id'])
        
        # Update the day object with relationships
        if 'relationships' not in db.data['days'][day_id]:
            db.data['days'][day_id]['relationships'] = {
                'places': linked_places,
                'expenses': linked_expenses
            }

if __name__ == '__main__':
    # Example usage: load existing data and apply relationships
    try:
        kit = TravelKitDB()
        kit.load('data.json')  # Assumes a standard structure from previous steps
        add_relationships(kit)
        kit.save('data.json')
    except FileNotFoundError:
        print("No existing data file found. Please initialize the project first.")
