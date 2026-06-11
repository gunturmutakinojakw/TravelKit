# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: TravelKit
def format_list_item(name, value):
    return f"• {name}: {value}" if isinstance(value, str) else f"• {name}: {len(value)} items"

def format_place(place):
    lines = [f"{place['name']}"]
    for key in ['city', 'country']:
        val = place.get(key)
        if val: lines.append(f"  - {key.capitalize()}: {val}")
    return "\n".join(lines)

def format_expense(exp):
    date_str = exp.get('date', 'Unknown')
    desc = exp.get('description', 'No description')
    amount = f"{exp['amount']:.2f}" if isinstance(exp['amount'], (int, float)) else str(exp['amount'])
    return f"[{date_str}] {desc} — {amount}"

def format_day_plan(day):
    lines = [f"Day {day.get('number', '?')}:"]
    for item in day.get('activities', []):
        loc = item.get('location', 'N/A')
        time = item.get('time', 'Anytime')
        desc = item.get('description', '')
        lines.append(f"  {loc} @ {time}")
        if desc: lines.append(f"    → {desc}")
    return "\n".join(lines)

def print_section_header(title):
    print("\n" + "=" * 40)
    print(f" {title.upper()}")
    print("=" * 40)
