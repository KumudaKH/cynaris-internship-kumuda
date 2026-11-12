import polars as pl
import time
import pandas as pd

DATA = "data/salary_100k.csv"

results = []

# Load dataset
start = time.time()

df = pl.read_csv(DATA)

load_time = time.time() - start

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# Five analytical operations
operations = {
    "Total Records": lambda: df.select(
        pl.len()
    ),

    "Average Salary": lambda: df.select(
        pl.col("Salary").mean()
    ),

    "Maximum Salary": lambda: df.select(
        pl.col("Salary").max()
    ),

    "Minimum Salary": lambda: df.select(
        pl.col("Salary").min()
    ),

    "Average Rating": lambda: df.select(
        pl.col("Rating").mean()
    )
}

for name, operation in operations.items():

    start = time.time()

    result = operation()

    execution_time = time.time() - start

    print(f"\n{name}")
    print(result)

    results.append({
        "Analysis": name,
        "Execution Time": execution_time,
        "Result": str(result)
    })

pd.DataFrame(results).to_csv(
    "results/polars_results.csv",
    index=False
)

print("\nPolars loading time:", load_time)