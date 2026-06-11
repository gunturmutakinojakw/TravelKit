# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: TravelKit
def sort_items(items, key='last_update'):
    if key == 'title': return sorted(items, key=lambda x: (x['priority'] or 0), reverse=True)
    if key == 'date': return sorted(items, key=lambda x: x.get('created_at', ''), reverse=True)
    if key == 'priority': return sorted(items, key=lambda x: (x['priority'] or 0), reverse=True)
    if key == 'last_update': return sorted(items, key=lambda x: x.get('updated_at', ''), reverse=True)
    return items
