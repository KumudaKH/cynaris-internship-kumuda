# W5D4: High-Performance DataFrame Operations

## Project Overview
This project compares three popular data analytics technologies: Pandas, DuckDB and Polars.

The objective is to evaluate their performance using a 100,000-row employee dataset and five analytical operations.

## Dataset
- Rows: 100,000
- Columns: 6
- Format: CSV
- File: employee_data_100k.csv

## Technologies
- Python
- Pandas
- DuckDB
- Polars
- NumPy
- Matplotlib

## Project Structure

```text
week5-day4/
│
├── employee_data_100k.csv
├── duckdb_analysis.py
├── duckdb_queries.py
├── pandas_analysis.py
├── polars_analysis.py
├── performance_chart.py
├── performance_comparison.png
├── comparison.md
└── README.md
```

## Analytical Operations

1. Department-wise employee count
2. Average salary by department
3. Top 10 highest-paid employees
4. Experience-wise average salary
5. Performance rating distribution

## Performance Comparison

| Operation | DuckDB (ms) | Pandas (ms) | Polars (ms) |
|---|---:|---:|---:|
| Department Count | 661.072 | 9.481 | 29.266 |
| Average Salary | 87.082 | 8.932 | 6.007 |
| Top 10 Salaries | 54.829 | 7.360 | 11.415 |
| Experience Analysis | 63.193 | 3.436 | 5.356 |
| Rating Distribution | 52.209 | 3.435 | 1.686 |

## Key Learnings

- Loading CSV files using DuckDB, Pandas and Polars.
- Performing analytical SQL queries.
- Applying DataFrame operations.
- Benchmarking execution times.
- Comparing different data processing technologies.
- Understanding columnar processing and OLAP workloads.

## Conclusion

Pandas is useful for general data manipulation, DuckDB is suitable for SQL-based analytical workloads, and Polars provides high-performance DataFrame processing.

The benchmark results are preliminary and depend on execution conditions, caching and implementation differences.