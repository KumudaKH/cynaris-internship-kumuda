import duckdb
import time
import pandas as pd
from pathlib import Path

DATA = "data/salary_100k.csv"

Path("results").mkdir(exist_ok=True)

con = duckdb.connect()

# Load CSV
start = time.time()

con.execute(f"""
    CREATE VIEW salary_data AS
    SELECT * FROM read_csv_auto('{DATA}')
""")

load_time = time.time() - start

print("Dataset loaded successfully!")
print("Rows:", con.execute(
    "SELECT COUNT(*) FROM salary_data"
).fetchone()[0])

# Display columns
print(con.execute(
    "DESCRIBE salary_data"
).fetchdf())

# Identify columns
columns = [
    row[0] for row in con.execute(
        "DESCRIBE salary_data"
    ).fetchall()
]

print("Available columns:", columns)

# Five analytical queries
queries = {
    "Total Records": """
        SELECT COUNT(*) AS total_records
        FROM salary_data
    """,

    "Average Salary": """
        SELECT AVG(salary) AS average_salary
        FROM salary_data
    """,

    "Maximum Salary": """
        SELECT MAX(salary) AS maximum_salary
        FROM salary_data
    """,

    "Minimum Salary": """
        SELECT MIN(salary) AS minimum_salary
        FROM salary_data
    """,

    "Average Rating": """
        SELECT AVG(rating) AS average_rating
        FROM salary_data
    """
}

# Execute queries
results = []

for name, query in queries.items():

    start = time.time()

    try:
        result = con.execute(query).fetchdf()
        execution_time = time.time() - start

        print(f"\n{name}")
        print(result)

        results.append({
            "Analysis": name,
            "Execution Time": execution_time,
            "Result": result.to_string(index=False)
        })

    except Exception as e:
        print(f"{name} could not execute: {e}")

pd.DataFrame(results).to_csv(
    "results/duckdb_results.csv",
    index=False
)

print("\nDuckDB loading time:", load_time)

con.close()