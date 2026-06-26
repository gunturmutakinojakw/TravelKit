# === Stage 56: Add compact error classes for domain failures ===
# Project: TravelKit
class TravelError(Exception):
    pass

class InvalidDate(TravelError):
    def __init__(self, date_str: str, reason: str = "Invalid format"):
        super().__init__(f"{reason}: {date_str}")
        self.date_str = date_str
        self.reason = reason

class MissingField(TravelError):
    def __init__(self, field_name: str, context: str = ""):
        msg = f"Missing required field: {field_name}"
        if context:
            msg += f" in {context}"
        super().__init__(msg)
        self.field_name = field_name
        self.context = context

class InvalidExpense(TravelError):
    def __init__(self, amount: float, currency: str, reason: str = "Invalid value"):
        if amount < 0:
            msg = f"Negative expense not allowed: {amount} {currency}"
        else:
            msg = f"{reason}: {amount} {currency}"
        super().__init__(msg)
        self.amount = amount
        self.currency = currency
        self.reason = reason

class DuplicatePlace(TravelError):
    def __init__(self, name: str, existing_ids: list[str]):
        msg = f"Duplicate place name '{name}' found. Existing IDs: {existing_ids}"
        super().__init__(msg)
        self.name = name
        self.existing_ids = existing_ids

class DayPlanConflict(TravelError):
    def __init__(self, day_id: int, activity_name: str, reason: str = "Time slot overlap"):
        msg = f"{reason} for '{activity_name}' on day {day_id}"
        super().__init__(msg)
        self.day_id = day_id
        self.activity_name = activity_name
        self.reason = reason

class PackingListError(TravelError):
    def __init__(self, item: str, category: str, error_type: str):
        msg = f"{error_type}: '{item}' in category '{category}'"
        super().__init__(msg)
        self.item = item
        self.category = category
        self.error_type = error_type
