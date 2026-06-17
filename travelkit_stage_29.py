# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: TravelKit
from datetime import datetime, timedelta
def get_upcoming_reminders(items: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).date()
    upcoming = []
    for item in items:
        due_date = datetime.strptime(item.get("due", ""), "%Y-%m-%d").date()
        if now <= due_date <= cutoff and not item.get("completed"):
            urgency = "urgent" if due_date - now.date() < timedelta(days=2) else "soon"
            upcoming.append({**item, "urgency": urgency})
    return sorted(upcoming, key=lambda x: x["due"])
