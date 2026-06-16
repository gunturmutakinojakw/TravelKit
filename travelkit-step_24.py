# === Stage 24: Add grouped summaries by category or status ===
# Project: TravelKit
def generate_grouped_summary(data, group_by='category'):
    grouped = {}
    for item in data:
        key = item.get(group_by)
        if key is None:
            key = 'Uncategorized'
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)

    total_amount = sum(i.get('amount', 0) for i in data)
    status_counts = {}
    for item in data:
        s = item.get('status') or 'pending'
        status_counts[s] = status_counts.get(s, 0) + 1

    print(f"Total Expenses: {total_amount:.2f}")
    if group_by == 'category':
        for cat, items in grouped.items():
            sum_cat = sum(i.get('amount', 0) for i in items)
            pending = len([i for i in items if (i.get('status') or 'pending') != 'paid'])
            print(f"  {cat}: {sum_cat:.2f} ({len(items)} items, {pending} unpaid)")
    else:
        for status, count in sorted(status_counts.items()):
            print(f"  Status '{status}': {count}")
