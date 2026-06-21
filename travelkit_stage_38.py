# === Stage 38: Add data integrity checks for broken references ===
# Project: TravelKit
def validate_references(db):
    required_refs = {'places': 'place_id', 'expenses': 'expense_place_id'}
    for table, ref_col in required_refs.items():
        missing_ids = set()
        if table == 'places': continue
        cursor = db.cursor()
        existing = {row[0] for row in cursor.execute(f"SELECT id FROM {table}").fetchall()}
        broken = [r for r, c in cursor.execute(f"SELECT DISTINCT {ref_col}, COUNT(*) as cnt FROM {table} GROUP BY {ref_col}") if c > 1 and r not in existing]
        if broken:
            print(f"[WARN] Broken references in {table}: {broken}")
            missing_ids.update(broken)
    cursor.close()

# === Stage 38: Add data integrity checks for broken references ===
# Project: TravelKit
def validate_integrity(data):
    if 'places' in data and 'expenses' in data:
        place_ids = {p['id'] for p in data.get('places', [])}
        expense_place_ids = {e['place_id'] for e in data.get('expenses', []) if isinstance(e, dict)}
        broken_refs = list(expense_place_ids - place_ids)
        if broken_refs:
            raise ValueError(f"Broken references found: expenses referencing non-existent places {broken_refs}")

    if 'day_plans' in data and 'places' in data:
        day_plan_place_ids = {dp['place_id'] for dp in data.get('day_plans', []) if isinstance(dp, dict)}
        broken_refs = list(day_plan_place_ids - place_ids)
        if broken_refs:
            raise ValueError(f"Broken references found: day plans referencing non-existent places {broken_refs}")

    return True
