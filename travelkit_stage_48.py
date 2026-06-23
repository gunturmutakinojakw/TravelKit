# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: TravelKit
import unittest


class TestTripHelpers(unittest.TestCase):
    def test_create_trip(self):
        trip = {"name": "Paris", "days": 5}
        self.assertEqual(trip["name"], "Paris")
        self.assertEqual(len(trip["days"]), 1)

    def test_validate_date_format(self):
        valid_dates = ["2024-01-01", "2023-12-31"]
        for date in valid_dates:
            with self.subTest(date=date):
                is_valid, msg = validate_date(date)
                self.assertTrue(is_valid, f"Expected {date} to be valid. Got: {msg}")

    def test_validate_invalid_date(self):
        invalid_dates = ["2024/13/45", "not-a-date"]
        for date in invalid_dates:
            with self.subTest(date=date):
                is_valid, msg = validate_date(date)
                self.assertFalse(is_valid)

    def test_validate_positive_amount(self):
        valid_amounts = [0.01, 100, 5000]
        for amount in valid_amounts:
            with self.subTest(amount=amount):
                is_valid, msg = validate_amount(amount)
                self.assertTrue(is_valid, f"Expected {amount} to be valid. Got: {msg}")

    def test_validate_negative_amount(self):
        invalid_amounts = [-10, -0.5]
        for amount in invalid_amounts:
            with self.subTest(amount=amount):
                is_valid, msg = validate_amount(amount)
                self.assertFalse(is_valid)


def validate_date(date_str):
    if not isinstance(date_str, str):
        return False, "Date must be a string"
    parts = date_str.split("-")
    if len(parts) != 3:
        return False, "Invalid date format. Expected YYYY-MM-DD"
    year, month, day = map(int, parts)
    if not (1 <= month <= 12):
        return False, f"Month must be between 1 and 12. Got {month}"
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    if not (1 <= day <= days_in_month[month - 1]):
        return False, f"Day must be between 1 and {days_in_month[month - 1]} for month {month}"
    return True, "Valid date"


def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        return False, "Amount must be a number"
    if amount < 0:
        return False, f"Amount cannot be negative. Got {amount}"
    return True, "Valid amount"
