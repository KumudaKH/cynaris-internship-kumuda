
import csv
import re
import sqlite3
from pathlib import Path

from vanna_setup import get_vanna

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "company.db"
RESULTS_PATH = BASE_DIR / "test_results.csv"

vn = get_vanna()

test_cases = [
    (
        "Which department has the highest average salary?",
        """SELECT department, AVG(salary) AS avg_salary
           FROM employees
           GROUP BY department
           ORDER BY avg_salary DESC
           LIMIT 1"""
    ),
    (
        "Show total monthly salary expense by department",
        """SELECT department, SUM(salary) AS total_salary
           FROM employees
           GROUP BY department
           ORDER BY total_salary DESC"""
    ),
    (
        "How many employees in each city earn above 40000?",
        """SELECT city, COUNT(*) AS employee_count
           FROM employees
           WHERE salary > 40000
           GROUP BY city
           ORDER BY city"""
    ),
    (
        "Show employees earning above their department average",
        """SELECT name, department, salary
           FROM employees e
           WHERE salary > (
               SELECT AVG(salary)
               FROM employees e2
               WHERE e2.department = e.department
           )
           ORDER BY salary DESC"""
    ),
    (
        "Which departments have at least 2 employees?",
        """SELECT department, COUNT(*) AS employee_count
           FROM employees
           GROUP BY department
           HAVING COUNT(*) >= 2
           ORDER BY department"""
    ),
    (
        "What is the average salary in the IT department?",
        """SELECT AVG(salary) AS avg_salary
           FROM employees
           WHERE department = 'IT'"""
    ),
    (
        "What is the total monthly salary expense of the company?",
        """SELECT SUM(salary) AS total_salary
           FROM employees"""
    ),
    (
        "Which city has the highest number of employees?",
        """SELECT city, COUNT(*) AS employee_count
           FROM employees
           GROUP BY city
           ORDER BY employee_count DESC, city
           LIMIT 1"""
    ),
    (
        "Show the top 3 highest-paid employees",
        """SELECT name, salary
           FROM employees
           ORDER BY salary DESC, name
           LIMIT 3"""
    ),
    (
        "Count employees in each department",
        """SELECT department, COUNT(*) AS employee_count
           FROM employees
           GROUP BY department
           ORDER BY department"""
    )
]


def execute_readonly(sql):
    sql = sql.strip()

    # Basic protection for local test data.
    if not re.match(r"^SELECT\b", sql, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed")

    if ";" in sql.rstrip(";"):
        raise ValueError("Multiple SQL statements are not allowed")

    db_uri = DB_PATH.resolve().as_uri() + "?mode=ro"

    with sqlite3.connect(db_uri, uri=True) as conn:
        conn.execute("PRAGMA query_only = ON")
        cursor = conn.execute(sql)
        return cursor.fetchall()


def normalize(rows):
    # Ignore column aliases and row ordering for
    # these sample-data comparisons.
    return sorted(repr(tuple(row)) for row in rows)


results = []

for index, (question, expected_sql) in enumerate(test_cases, 1):
    print(f"\nTest {index}: {question}")

    generated_sql = ""

    try:
        generated_sql = vn.generate_sql(
            question=question,
            allow_llm_to_see_data=False
        )

        if not generated_sql:
            raise ValueError("Vanna returned no SQL")

        generated_rows = execute_readonly(generated_sql)
        expected_rows = execute_readonly(expected_sql)

        passed = normalize(generated_rows) == normalize(expected_rows)
        status = "PASS" if passed else "FAIL"

        print("Generated SQL:", generated_sql)
        print("Expected:", expected_rows)
        print("Actual:", generated_rows)
        print("Result:", status)

    except Exception as error:
        status = "ERROR"
        print("Error:", error)

    results.append({
        "test_number": index,
        "question": question,
        "generated_sql": generated_sql,
        "expected_sql": expected_sql,
        "status": status
    })

with open(RESULTS_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

passed_count = sum(r["status"] == "PASS" for r in results)

print("\n==============================")
print("W6D2 TEST SUMMARY")
print("==============================")
print(f"Total Tests: {len(results)}")
print(f"Passed: {passed_count}")
print(f"Failed/Errors: {len(results) - passed_count}")
print(f"Results saved to: {RESULTS_PATH}")
