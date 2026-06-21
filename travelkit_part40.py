# === Stage 40: Add plain text report export ===
# Project: TravelKit
def export_report(trip_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Trip Summary\n")
        f.write("=" * 40 + "\n")
        for day in trip_data.get('days', []):
            f.write(f"\nDay {day['date']}\n")
            if 'places' in day and day['places']:
                for place in day['places']:
                    f.write(f"  - {place['name']} ({place['category']})\n")
            if 'notes' in day:
                f.write(f"\nNotes:\n{day['notes']}\n")
        total_expenses = sum(day.get('expenses', {}).get('total', 0) for day in trip_data.get('days', []))
        f.write("\n" + "=" * 40 + "\n")
        f.write(f"Total Expenses: {total_expenses:.2f}\n")
