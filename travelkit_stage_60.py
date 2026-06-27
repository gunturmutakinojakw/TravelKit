# === Stage 60: Add saved views for frequently used filters ===
# Project: TravelKit
class SavedViewManager:
    def __init__(self, db):
        self.db = db
        
    def save_view(self, name, filters=None, sort_by=None):
        if filters is None:
            filters = {}
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO saved_views (name, json_filters, json_sort)
                VALUES (%s, %s, %s)
                ON CONFLICT(name) DO UPDATE SET 
                    json_filters = EXCLUDED.json_filters,
                    json_sort = EXCLUDED.json_sort
            """, (name, self._serialize(filters), self._serialize(sort_by)))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            cursor.close()

    def load_view(self, name):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT json_filters, json_sort FROM saved_views WHERE name = %s", (name,))
            row = cursor.fetchone()
            if not row:
                return None
            filters = self._deserialize(row[0]) or {}
            sort_by = self._deserialize(row[1]) or {}
            return {"filters": filters, "sort_by": sort_by}
        finally:
            cursor.close()

    def delete_view(self, name):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM saved_views WHERE name = %s", (name,))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            cursor.close()

    def list_views(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT name FROM saved_views ORDER BY created_at DESC")
            return [row[0] for row in cursor.fetchall()]
        finally:
            cursor.close()

    @staticmethod
    def _serialize(obj):
        import json
        if obj is None:
            return "null"
        try:
            return json.dumps(obj, sort_keys=True)
        except TypeError:
            return str(obj)

    @staticmethod
    def _deserialize(data):
        if data == "null":
            return None
        try:
            import json
            return json.loads(data)
        except (json.JSONDecodeError, ValueError):
            return {}
