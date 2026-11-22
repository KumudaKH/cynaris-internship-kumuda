from pathlib import Path
import sqlite3
import csv
BASE = Path(__file__).resolve().parent
with sqlite3.connect(BASE / "company.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS employees (employee_id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary INTEGER, city TEXT)")
    with (BASE / "employees.csv").open(newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))
    conn.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?, ?)", [(int(r["employee_id"]), r["name"], r["department"], int(r["salary"]), r["city"]) for r in records])
print("Database ready")
