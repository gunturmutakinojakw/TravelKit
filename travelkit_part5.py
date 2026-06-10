# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: TravelKit
def update_item(item_type, item_id, new_data):
    """
    Updates an existing record in the trip database.
    Handles missing records by logging a warning and returning False.
    Supports: 'packing', 'place', 'expense', 'day_plan'.
    """
    db = get_db()
    if not db:
        return False

    table_map = {
        'packing': 'packing_list',
        'place': 'places',
        'expense': 'expenses',
        'day_plan': 'day_plans'
    }

    table_name = table_map.get(item_type)
    if not table_name:
        print(f"Unknown item type: {item_type}")
        return False

    # Construct the update query dynamically based on provided keys
    set_clauses = []
    for key, value in new_data.items():
        set_clauses.append(f"{key} = :{key}")

    if not set_clauses:
        print("No data to update.")
        return False

    query = f"""
        UPDATE {table_name}
        SET {', '.join(set_clauses)}
        WHERE id = :id
    """

    try:
        cursor = db.cursor()
        params = {k: v for k, v in new_data.items()}
        params['id'] = item_id
        cursor.execute(query, params)
        db.commit()

        if cursor.rowcount == 0:
            print(f"Warning: No record found with id={item_id} in table={table_name}.")
            return False

        return True

    except Exception as e:
        db.rollback()
        print(f"Error updating {item_type}: {e}")
        return False
