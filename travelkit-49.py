# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: TravelKit
import unittest
from travelkit import TravelKit

class TestTravelKitEdgeCases(unittest.TestCase):
    def setUp(self):
        self.kit = TravelKit("test_trip")

    def test_update_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.kit.update_place("non_existent_id", {"name": "New Name"})

    def test_delete_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.kit.delete_expense("non_existent_id")

    def test_update_with_empty_data_removes_fields(self):
        place = self.kit.create_place(name="Paris")
        self.kit.update_place(place.id, {"name": "Paris"})
        updated = self.kit.get_place(place.id)
        self.assertEqual(updated["name"], "Paris")

    def test_delete_then_update_raises_error(self):
        expense = self.kit.add_expense(amount=50.0, category="Food")
        self.kit.delete_expense(expense.id)
        with self.assertRaises(ValueError):
            self.kit.update_expense(expense.id, {"amount": 100.0})

    def test_update_place_preserves_other_fields(self):
        place = self.kit.create_place(name="London", country="UK")
        self.kit.update_place(place.id, {"name": "New London"})
        updated = self.kit.get_place(place.id)
        self.assertEqual(updated["country"], "UK")

if __name__ == "__main__":
    unittest.main()
