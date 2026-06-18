# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: TravelKit
from datetime import date, timedelta
import re

def parse_date_input(user_str: str) -> date | None:
    """Parse common date formats and return a date object or raise ValueError."""
    patterns = [
        (r'^(\d{4})-(\d{2})-(\d{2})$', lambda m: date(int(m[1]), int(m[2]), int(m[3]))),  # YYYY-MM-DD
        (r'^(\d{2})/(\d{2})/(\d{4})$', lambda m: date(int(m[3]), int(m[1]), int(m[2]))),   # MM/DD/YYYY
        (r'^(\d{2})\.(\d{2})\.(\d{4})$', lambda m: date(int(m[3]), int(m[1]), int(m[2]))),  # DD.MM.YYYY
    ]
    for pattern, parser in patterns:
        match = re.match(pattern, user_str.strip())
        if match:
            try:
                return parser(match)
            except ValueError as e:
                raise ValueError(f"Invalid date components from '{user_str}': {e}")
    raise ValueError(f"Unrecognized date format: '{user_str}'. Expected YYYY-MM-DD or similar.")

def get_week_around(target_date: date, offset_days: int = 0) -> list[date]:
    """Return a list of dates centered on target_date with given offset."""
    start = target_date - timedelta(days=offset_days)
    end = target_date + timedelta(days=offset_days)
    return [start + timedelta(days=i) for i in range((end - start).days + 1)]

def is_valid_travel_date(year: int, month: int, day: int) -> bool:
    """Check if a date exists without raising exceptions."""
    try:
        d = date(year, month, day)
        return True
    except ValueError:
        return False
