# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: TravelKit
def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a monetary amount with locale-aware symbols and two decimal places."""
    if currency == "EUR":
        symbol = "€"
    elif currency == "GBP":
        symbol = "£"
    else:
        symbol = "$"
    return f"{symbol}{amount:.2f}"

def validate_date_input(date_str: str) -> tuple[bool, str]:
    """Parse a date string in YYYY-MM-DD format and return validity status with error message."""
    import re
    pattern = r"^(\d{4})-(\d{2})-(\d{2})$"
    match = re.match(pattern, date_str)
    if not match:
        return False, "Invalid date format. Expected YYYY-MM-DD."
    year, month, day = map(int, match.groups())
    if month < 1 or month > 12:
        return False, f"Month must be between 01 and 12, got {month}."
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    if day < 1 or day > days_in_month[month - 1]:
        return False, f"Day {day} is not valid for month {month}."
    return True, "Date is valid."

def generate_day_plan_template(day: int) -> dict[str, str | None]:
    """Generate a structured dictionary template for a single day's itinerary."""
    activities = ["Morning", "Afternoon", "Evening"]
    locations = [None] * len(activities)
    notes = [None] * len(activities)
    return {
        "day": day,
        "morning": {"activity": None, "location": locations[0], "notes": notes[0]},
        "afternoon": {"activity": None, "location": locations[1], "notes": notes[1]},
        "evening": {"activity": None, "location": locations[2], "notes": notes[2]}
    }

def calculate_total_expenses(expense_list: list[dict]) -> float:
    """Sum up all expenses from a list of dictionaries containing 'amount' keys."""
    return sum(item.get("amount", 0) for item in expense_list if isinstance(item, dict))
