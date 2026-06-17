# === Stage 27: Add monthly summary calculations ===
# Project: TravelKit
def calculate_monthly_summary(trip_data):
    from collections import defaultdict
    monthly_expenses = defaultdict(float)
    for day_plan in trip_data.get("day_plans", []):
        date_str = day_plan.get("date") or ""
        if not date_str: continue
        month_key = f"{date_str[:4]}-{date_str[5:7]}"
        expenses = day_plan.get("expenses", [])
        for expense in expenses:
            amount = float(expense.get("amount", 0))
            category = expense.get("category", "other")
            monthly_expenses[month_key] += amount
    
    summary_list = []
    for month, total in sorted(monthly_expenses.items()):
        entry = {
            "month": month,
            "total_spent": round(total, 2),
            "categories": {},
        }
        # Aggregate categories per month if needed or store flat list
        # Here we just keep the total for simplicity as requested compact block
        summary_list.append(entry)
    
    trip_data["monthly_summary"] = summary_list
    return trip_data
