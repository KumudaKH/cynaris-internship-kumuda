import matplotlib.pyplot as plt
import numpy as np

operations = [
    "Department Count",
    "Average Salary",
    "Top 10 Salaries",
    "Experience Analysis",
    "Rating Distribution"
]

duckdb = [661.072, 87.082, 54.829, 63.193, 52.209]
pandas = [9.481, 8.932, 7.360, 3.436, 3.435]
polars = [29.266, 6.007, 11.415, 5.356, 1.686]

x = np.arange(len(operations))
width = 0.25

plt.figure(figsize=(12, 6))

plt.bar(x - width, duckdb, width, label="DuckDB")
plt.bar(x, pandas, width, label="Pandas")
plt.bar(x + width, polars, width, label="Polars")

plt.xlabel("Analytical Operations")
plt.ylabel("Execution Time (ms)")
plt.title("Pandas vs DuckDB vs Polars Performance Comparison")

plt.xticks(x, operations, rotation=15)
plt.legend()
plt.tight_layout()

plt.savefig("performance_comparison.png", dpi=300)

plt.show()

print("Performance comparison chart saved successfully!")