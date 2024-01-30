"""Utils for opus database."""
import sqlite3

class SQLiteDB():
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()