# === Stage 51: Add unit tests for search and filter behavior ===
# Project: TravelKit
import unittest
from travelkit import TripManager, Item, Place, Expense, DayPlan

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.trip = TripManager()
        self.trip.add_item(Item("Passport", "Travel Doc"))
        self.trip.add_item(Item("Sunscreen", "Clothing"), category="clothing")
        self.trip.add_place(Place("Paris", 10.0))
        self.trip.add_expense(Expense("Hotel", 200.0, "Accommodation"))
        self.trip.add_day_plan(DayPlan("Day 1", ["Eiffel Tower"], budget=50.0))

    def test_search_by_name(self):
        results = self.trip.search_items("sun")
        self.assertEqual(len(results), 1)
        self.assertIn("Sunscreen", [i.name for i in results])

    def test_filter_by_category(self):
        clothing = self.trip.filter_items(category="clothing")
        self.assertTrue(any(i.category == "clothing" for i in clothing))

    def test_search_places_by_city(self):
        paris = self.trip.search_places("Paris")
        self.assertEqual(len(paris), 1)
        self.assertEqual(paris[0].city, "Paris")

    def test_filter_expenses_by_type(self):
        housing = self.trip.filter_expenses(type="Accommodation")
        self.assertTrue(any(e.type == "Accommodation" for e in housing))
