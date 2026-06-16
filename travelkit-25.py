# === Stage 25: Add daily summary calculations ===
# Project: TravelKit
def calculate_daily_summary(day_plan):
    total_expenses = sum(item.get('amount', 0) for item in day_plan.get('expenses', []))
    activities_count = len(day_plan.get('activities', []))
    places_visited = list(set(place['name'] for place in day_plan.get('places', []) if 'visited' in place and place['visited']))
    summary = {
        'date': day_plan.get('date'),
        'total_expenses': total_expenses,
        'activities_count': activities_count,
        'places_visited_count': len(places_visited),
        'notes': day_plan.get('notes', '')
    }
    return summary

def generate_weekly_report(trip_data):
    daily_summaries = [calculate_daily_summary(day) for day in trip_data.get('days', [])]
    weekly_total_expenses = sum(summary['total_expenses'] for summary in daily_summaries)
    weekly_activities_count = sum(summary['activities_count'] for summary in daily_summaries)
    all_places_visited = []
    seen_places = set()
    for day_summary in daily_summaries:
        places_on_day = [p['name'] for p in trip_data.get('places', []) if 'visited' in p and p['visited']]
        # Note: This simplified logic assumes places list is global; ideally pass specific visited list per day summary
        all_places_visited.extend([p['name'] for p in trip_data.get('places', []) if 'visited' in p and p['visited']])
    weekly_report = {
        'week_start': daily_summaries[0]['date'],
        'week_end': daily_summaries[-1]['date'],
        'total_expenses': weekly_total_expenses,
        'total_activities': weekly_activities_count,
        'unique_places_visited': len(set(all_places_visited))
    }
    return weekly_report
