import polars as pl
import time

# Load dataset
start = time.perf_counter()

df = pl.read_csv("employee_data_100k.csv")

load_time = (time.perf_counter() - start) * 1000

print("Dataset loaded successfully using Polars!")
print("Dataset Shape:", df.shape)

# Five analytical operations
operations = {
    "Query 1 - Department-wise Employee Count":
        lambda: df.group_by("department").len(),

    "Query 2 - Average Salary by Department":
        lambda: df.group_by("department").agg(
            pl.col("salary").mean().alias("average_salary")
        ),

    "Query 3 - Top 10 Highest Paid Employees":
        lambda: df.sort("salary", descending=True).head(10).select(
            ["employee_id", "department", "salary"]
        ),

    "Query 4 - Experience-wise Average Salary":
        lambda: df.group_by("experience").agg(
            pl.col("salary").mean().alias("average_salary")
        ).sort("experience"),

    "Query 5 - Performance Rating Distribution":
        lambda: df.group_by("performance_rating").len().sort(
            "performance_rating"
        )
}

results = []

for name, operation in operations.items():

    start = time.perf_counter()

    result = operation()

    end = time.perf_counter()

    execution_time = (end - start) * 1000

    results.append({
        "Query": name,
        "Execution Time (ms)": round(execution_time, 3)
    })

    print("\n", "=" * 60)
    print(name)
    print(result)
    print("Execution Time:", round(execution_time, 3), "ms")

print("\nPOLARS PERFORMANCE SUMMARY")

for item in results:
    print(item)

print("\nCSV Loading Time:", round(load_time, 3), "ms")