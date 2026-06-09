# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: TravelKit
class TravelKit:
    def __init__(self):
        self.places = {"Paris": "France", "Tokyo": "Japan"}
        self.expenses = {}
        self.packing = []
        self.day_plans = {}

    def add_place(self, name, country):
        self.places[name] = country

    def log_expense(self, place, amount):
        if place not in self.expenses:
            self.expenses[place] = 0.0
        self.expenses[place] += float(amount)

    def add_item(self, item):
        self.packing.append(item)

    def set_day_plan(self, day, activities):
        self.day_plans[day] = activities

kit = TravelKit()
kit.add_place("Paris", "France")
kit.log_expense("Paris", 45.0)
kit.add_item("Passport")
kit.set_day_plan(1, ["Museum", "Lunch"])
print(f"Places: {kit.places}")
print(f"Expenses: {kit.expenses}")
print(f"Packing: {kit.packing}")
print(f"Day 1 Plan: {kit.day_plans.get(1)}")
