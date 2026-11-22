
import csv
import re
import sqlite3
from pathlib import Path
from vanna_setup import get_vanna

BASE_DIR = Path(__file__).resolve().parent
vn = get_vanna()

questions = [
    ("Show all employees",
     "SELECT * FROM employees"),

    ("Show employees working in IT",
     "SELECT * FROM employees WHERE department = 'IT'"),

    ("Count the total number of employees",
     "SELECT COUNT(*) AS total FROM employees"),

    ("Find the average employee salary",
     "SELECT AVG(salary) AS average_salary FROM employees"),

    ("Show the highest paid employee",
     "SELECT * FROM employees ORDER BY salary DESC LIMIT 1"),

    ("Show employees earning more than 40000",
     "SELECT * FROM employees WHERE salary > 40000"),

    ("Count employees in each department",
     "SELECT department, COUNT(*) AS total FROM employees GROUP BY department"),

    ("Show employees from Bangalore",
     "SELECT * FROM employees WHERE city = 'Bangalore'"),

    ("Find the minimum salary",
     "SELECT MIN(salary) AS minimum_salary FROM employees"),

    ("Show the top 3 highest paid employees",
     "SELECT * FROM employees ORDER BY salary DESC LIMIT 3")
]

def execute_sql(sql):
    sql = sql.strip()

    if not re.match(r"^SELECT\b", sql, re.I):
        raise ValueError("Only SELECT queries are allowed")

    if sql.count(";") > 1 or ";" in sql.rstrip(";"):
        raise ValueError("Multiple statements are not allowed")

    db_uri = (BASE_DIR / "company.db").as_uri() + "?mode=ro"

    with sqlite3.connect(db_uri, uri=True) as conn:
        conn.execute("PRAGMA query_only = ON")
        return conn.execute(sql).fetchall()

results = []

for number, (question, expected_sql) in enumerate(questions, 1):
    print(f"\nTEST {number}: {question}")

    generated_sql = ""
    status = "ERROR"

    try:
        generated_sql = vn.generate_sql(
            question=question,
            allow_llm_to_see_data=False
        )

        if not isinstance(generated_sql, str):
            raise ValueError("No SQL generated")

        actual = execute_sql(generated_sql)
        expected = execute_sql(expected_sql)

        if "ORDER BY" in expected_sql.upper():
            passed = actual == expected
        else:
            passed = sorted(map(str, actual)) == sorted(map(str, expected))

        status = "PASS" if passed else "FAIL"

        print("Generated SQL:", generated_sql)
        print("Output:", actual)
        print("Status:", status)

    except Exception as error:
        print("Error:", error)

    results.append({
        "question": question,
        "expected_sql": expected_sql,
        "generated_sql": generated_sql,
        "status": status
    })

with open(BASE_DIR / "test_results.csv", "w",
          newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file, fieldnames=results[0].keys()
    )
    writer.writeheader()
    writer.writerows(results)

print("\n--- FINAL TEST SUMMARY ---")
print("Total tests:", len(results))
print("Passed:", sum(r["status"] == "PASS" for r in results))
print("Failed:", sum(r["status"] == "FAIL" for r in results))
print("Errors:", sum(r["status"] == "ERROR" for r in results))
print("Results saved to test_results.csv")
