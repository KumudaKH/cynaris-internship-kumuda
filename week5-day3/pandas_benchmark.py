import pandas as pd
import time

DATA = "data/salary_100k.csv"

start = time.time()

df = pd.read_csv(DATA)

load_time = time.time() - start

print("Dataset loaded:", df.shape)

results = []

operations = {
    "Total Records": lambda: len(df),
    "Average Salary": lambda: df["Salary"].mean(),
    "Maximum Salary": lambda: df["Salary"].max(),
    "Minimum Salary": lambda: df["Salary"].min(),
    "Average Rating": lambda: df["Rating"].mean()
}

for name, operation in operations.items():

    start = time.time()

    result = operation()

    execution_time = time.time() - start

    print(f"\n{name}: {result}")
    print("Execution time:", execution_time)

    results.append({
        "Analysis": name,
        "Execution Time": execution_time,
        "Result": result
    })

pd.DataFrame(results).to_csv(
    "results/pandas_results.csv",
    index=False
)

print("\nPandas loading time:", load_time)
