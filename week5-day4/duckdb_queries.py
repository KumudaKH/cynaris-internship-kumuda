import duckdb
import time

# Connect to DuckDB
con = duckdb.connect(database=":memory:")

# Load CSV into DuckDB
con.execute("""
    CREATE VIEW employees AS
    SELECT * FROM read_csv_auto('employee_data_100k.csv')
""")

print("Dataset loaded successfully into DuckDB!")

# Five analytical SQL queries
queries = {
    "Query 1 - Department-wise Employee Count": """
        SELECT department, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
        ORDER BY employee_count DESC
    """,

    "Query 2 - Average Salary by Department": """
        SELECT department, ROUND(AVG(salary), 2) AS average_salary
        FROM employees
        GROUP BY department
        ORDER BY average_salary DESC
    """,

    "Query 3 - Top 10 Highest Paid Employees": """
        SELECT employee_id, department, salary
        FROM employees
        ORDER BY salary DESC
        LIMIT 10
    """,

    "Query 4 - Experience-wise Average Salary": """
        SELECT experience, ROUND(AVG(salary), 2) AS average_salary
        FROM employees
        GROUP BY experience
        ORDER BY experience
    """,

    "Query 5 - Performance Rating Distribution": """
        SELECT performance_rating, COUNT(*) AS employee_count
        FROM employees
        GROUP BY performance_rating
        ORDER BY performance_rating
    """
}

# Execute and benchmark queries
results = []

for name, query in queries.items():
    start = time.perf_counter()

    result = con.execute(query).df()

    end = time.perf_counter()

    execution_time = (end - start) * 1000

    results.append({
        "Query": name,
        "Execution Time (ms)": round(execution_time, 3)
    })

    print("\n", "=" * 60)
    print(name)
    print(result.to_string(index=False))
    print("Execution Time:", round(execution_time, 3), "ms")

print("\n\nDUCKDB PERFORMANCE SUMMARY")
for item in results:
    print(item)

con.close()