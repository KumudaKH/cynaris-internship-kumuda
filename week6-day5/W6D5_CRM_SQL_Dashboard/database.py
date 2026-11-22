from pathlib import Path
import sqlite3
DB_PATH = Path(__file__).resolve().parent / "crm.db"

def check_database():
    with sqlite3.connect(DB_PATH) as conn:
        for table in ("customers", "opportunities"):
            print(table, conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])

if __name__ == "__main__":
    check_database()
