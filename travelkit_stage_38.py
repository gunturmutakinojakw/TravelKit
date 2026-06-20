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
