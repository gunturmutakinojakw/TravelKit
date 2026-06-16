# === Stage 26: Add weekly summary calculations ===
# Project: TravelKit
def calculate_weekly_summary(trip_data):
    weekly_expenses = {}
    for day, record in trip_data.get('expenses', {}).items():
        week_num = (int(day.split('-')[2]) - 1) // 7 + 1
        amount = float(record['amount']) if isinstance(record['amount'], str) else record['amount']
        category = record.get('category', 'Other')
        weekly_expenses.setdefault(week_num, {}).setdefault(category, 0.0)
        weekly_expenses[week_num][category] += amount
    
    summary_report = []
    for week in sorted(weekly_expenses.keys()):
        total_week = sum(weekly_expenses[week].values())
        items = list(weekly_expenses[week].items())
        if not items: continue
        category_order, amounts = zip(*sorted(items, key=lambda x: -x[1]))
        summary_report.append({
            'week': week,
            'total': total_week,
            'breakdown': dict(zip(category_order, amounts))
        })
    
    trip_data['weekly_summary'] = summary_report
    return trip_data
