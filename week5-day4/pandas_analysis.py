import pandas as pd
import time

# Load dataset
start = time.perf_counter()

df = pd.read_csv("employee_data_100k.csv")

load_time = (time.perf_counter() - start) * 1000

print("Dataset loaded successfully using Pandas!")
print("Dataset Shape:", df.shape)

# Five analytical operations
operations = {
    "Query 1 - Department-wise Employee Count":
        lambda: df.groupby("department").size().reset_index(name="employee_count"),

    "Query 2 - Average Salary by Department":
        lambda: df.groupby("department")["salary"].mean().reset_index(name="average_salary"),

    "Query 3 - Top 10 Highest Paid Employees":
        lambda: df.nlargest(10, "salary")[["employee_id", "department", "salary"]],

    "Query 4 - Experience-wise Average Salary":
        lambda: df.groupby("experience")["salary"].mean().reset_index(name="average_salary"),

    "Query 5 - Performance Rating Distribution":
        lambda: df.groupby("performance_rating").size().reset_index(name="employee_count")
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
    print(result.to_string(index=False))
    print("Execution Time:", round(execution_time, 3), "ms")

print("\nPANDAS PERFORMANCE SUMMARY")

for item in results:
    print(item)

print("\nCSV Loading Time:", round(load_time, 3), "ms")