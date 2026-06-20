# === Stage 37: Add recommendations for the next useful action ===
# Project: TravelKit
def get_next_action(trip_plan, current_day):
    if current_day < trip_plan['days']:
        day = trip_plan['days'] - 1 + current_day
        return f"Prepare for Day {day}: Review itinerary and pack essentials."
    elif not trip_plan.get('expenses', []):
        return "Review budget: No expenses recorded yet. Add your first expense."
    else:
        total = sum(e['amount'] for e in trip_plan['expenses'])
        remaining = trip_plan['budget'] - total
        if remaining < 0:
            return f"Budget Alert: You are {abs(remaining)} over budget. Review expenses immediately."
        elif remaining > trip_plan['budget'] * 0.5 and len(trip_plan.get('places', [])) == 1:
            return "Explore more: Consider adding a new place to your itinerary."
        else:
            return "Enjoy your trip! Check in with friends or log any new experiences."

if __name__ == "__main__":
    sample_trip = {
        'days': 5,
        'budget': 1000.0,
        'expenses': [{'amount': 200}, {'amount': 300}],
        'places': ['Paris']
    }
    print(get_next_action(sample_trip, 4))
