# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: TravelKit
def run_demo():
    trip = Trip("Summer Hike", "Alps")
    day1_plan = DayPlan(1, ["Arrival", "Check-in"])
    day2_plan = DayPlan(2, ["Hiking Trail A", "Picnic"])
    trip.add_day(day1_plan)
    trip.add_day(day2_plan)

    items = [Item("Backpack"), Item("Water Bottle")]
    packing_list = PackingList(trip.name, items)
    trip.set_packing(packing_list)

    places = [Place("Mountain Lodge", "Basecamp"), Place("Summit View", "Peak")]
    trip.add_places(places)

    expenses = Expense("Transport", 50.0), Expense("Food", 25.0)
    trip.set_expenses(expenses)

    print(f"Trip: {trip.name} at {trip.location}")
    for day in trip.days:
        print(f"Day {day.day}: {', '.join(day.activities)}")
    print(f"Packing: {[i.name for i in packing_list.items]}")
    print(f"Places: {[p.name for p in trip.places]}")
    print(f"Expenses: {sum(e.amount for e in trip.expenses):.2f}")
