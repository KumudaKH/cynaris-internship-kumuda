
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
conn = sqlite3.connect(BASE_DIR / "company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    city TEXT NOT NULL
)
""")

employees = [
    (1, "Rahul", "IT", 45000, "Bangalore"),
    (2, "Priya", "HR", 35000, "Chennai"),
    (3, "Amit", "IT", 55000, "Bangalore"),
    (4, "Sneha", "Finance", 50000, "Mumbai"),
    (5, "Kiran", "IT", 40000, "Hyderabad"),
    (6, "Anjali", "HR", 38000, "Bangalore"),
    (7, "Ravi", "Finance", 60000, "Delhi"),
    (8, "Pooja", "IT", 48000, "Chennai"),
    (9, "Arjun", "Sales", 32000, "Bangalore"),
    (10, "Meena", "Sales", 36000, "Mumbai")
]

cursor.executemany("""
INSERT OR REPLACE INTO employees
(employee_id, name, department, salary, city)
VALUES (?, ?, ?, ?, ?)
""", employees)

conn.commit()

print("SQLite database created successfully!")

for row in cursor.execute("SELECT * FROM employees"):
    print(row)

conn.close()
