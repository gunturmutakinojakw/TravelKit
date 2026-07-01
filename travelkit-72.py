# === Stage 72: Add Markdown report export ===
# Project: TravelKit
def export_report(trip_data):
    from datetime import date
    today = date.today()
    report_lines = [f"# TravelKit Report: {trip_data['name']} ({today.strftime('%Y-%m-%d')})"]
    if 'places' in trip_data and trip_data['places']:
        report_lines.append("## Places")
        for place in sorted(trip_data['places'], key=lambda x: x.get('day', 0)):
            report_lines.append(f"- **{place['name']}**: {place.get('notes', '')}")
    if 'expenses' in trip_data and trip_data['expenses']:
        total = sum(e['amount'] for e in trip_data['expenses'])
        report_lines.append("## Expenses")
        for exp in sorted(trip_data['expenses'], key=lambda x: x.get('date', '')):
            report_lines.append(f"- {exp['category']}: {exp['amount']} ({exp['date']})")
        report_lines.append(f"**Total**: {total:.2f}")
    if 'packing' in trip_data and trip_data['packing']:
        report_lines.append("## Packing List")
        for item, qty in sorted(trip_data['packing'].items()):
            report_lines.append(f"- [{qty}] {item}")
    return "\n".join(report_lines)
