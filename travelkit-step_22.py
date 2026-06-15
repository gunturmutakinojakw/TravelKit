# === Stage 22: Add favorite records and quick favorite listing ===
# Project: TravelKit
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_type TEXT NOT NULL,
                item_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db.commit()

    def add_favorite(self, item_type, item_id):
        try:
            self.cursor.execute(
                'INSERT INTO favorites (item_type, item_id) VALUES (?, ?)',
                (item_type, item_id)
            )
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_favorites(self):
        self.cursor.execute('SELECT * FROM favorites ORDER BY created_at DESC')
        return self.cursor.fetchall()

    def remove_favorite(self, item_type, item_id):
        try:
            self.cursor.execute(
                'DELETE FROM favorites WHERE item_type = ? AND item_id = ?',
                (item_type, item_id)
            )
            self.db.commit()
            return True
        except sqlite3.Error:
            return False

    def close(self):
        self.db.close()
