# === Stage 28: Add overdue item detection based on due dates ===
# Project: TravelKit
from datetime import date, timedelta

def check_overdue_items(items):
    today = date.today()
    overdue = []
    for item in items:
        due_date_str = item.get("due_date")
        if due_date_str:
            try:
                due_date = date.fromisoformat(due_date_str)
                if due_date < today and not item.get("completed", False):
                    overdue.append({
                        "name": item["name"],
                        "days_overdue": (today - due_date).days,
                        "category": item.get("category")
                    })
            except ValueError:
                pass
    return overdue

if __name__ == "__main__":
    sample_items = [
        {"name": "Passport", "completed": False, "due_date": "2023-10-01"},
        {"name": "Sunscreen", "completed": True, "due_date": "2024-05-15"},
        {"name": "Adapters", "completed": False, "due_date": date.today().isoformat()}
    ]
    
    overdue_list = check_overdue_items(sample_items)
    
    if overdue_list:
        print("Overdue items detected:")
        for item in overdue_list:
            print(f"- {item['name']} ({item['category']}) is {item['days_overdue']} days overdue")
    else:
        print("No overdue items found.")
