# === Stage 66: Add export of a short status dashboard ===
# Project: TravelKit
def export_status_dashboard(trip, users):
    from datetime import datetime
    total_expenses = sum(u.get('expenses', {}).get('total', 0) for u in users.values())
    items_count = len(set(item for user in users.values() for item in user.get('packing_list', [])))
    places_visited = set(place['name'] for user in users.values() for place in user.get('places', []) if place.get('status') == 'visited')
    days_planned = sum(len(day) for day in trip.get('day_plan', {}).values())
    status = "On Track" if total_expenses < 500 else "Budget Alert"
    print(f"\n=== TravelKit Status Dashboard ===")
    print(f"Trip: {trip['name']} | Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"Packing Items: {items_count}")
    print(f"Places Visited: {len(places_visited)} ({', '.join(sorted(places_visited))})")
    print(f"Days Planned: {days_planned}")
    print(f"Total Expenses: ${total_expenses:.2f} [{status}]")
