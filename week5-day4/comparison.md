# W5D4: High-Performance DataFrame Operations

## Objective
Compare Pandas, DuckDB and Polars using a 100,000-row employee dataset.

## Dataset Information
- Total Rows: 100,000
- Total Columns: 6
- File: employee_data_100k.csv

## Technologies Used
- Python
- Pandas
- DuckDB
- Polars
- NumPy
- Matplotlib

## Performance Results

| Operation | DuckDB (ms) | Pandas (ms) | Polars (ms) |
|---|---:|---:|---:|
| Department Count | 661.072 | 9.481 | 29.266 |
| Average Salary | 87.082 | 8.932 | 6.007 |
| Top 10 Salaries | 54.829 | 7.360 | 11.415 |
| Experience Analysis | 63.193 | 3.436 | 5.356 |
| Rating Distribution | 52.209 | 3.435 | 1.686 |

## Comparison

| Criteria | Pandas | DuckDB | Polars |
|---|---|---|---|
| Language | Python | SQL | Python/SQL |
| Processing | In-memory | Columnar engine | Columnar engine |
| Performance | Good | Excellent for analytical SQL | High |
| Memory | Can be high | Efficient | Generally efficient |
| Usage | Data analysis | SQL analytics | Fast DataFrames |

## Key Learnings
1. Learned to load CSV datasets using three different technologies.
2. Executed five analytical operations using each technology.
3. Learned SQL-based analytics using DuckDB.
4. Practised DataFrame operations using Pandas and Polars.
5. Compared execution times and programming syntax.
6. Understood columnar processing and analytical workloads.

## Conclusion
Pandas, DuckDB and Polars are useful tools for data analytics. Pandas provides a familiar interface for data manipulation, DuckDB supports SQL-based analytical processing, and Polars provides high-performance DataFrame operations.

The benchmark results are preliminary because the loading and execution measurements are not fully equivalent. More controlled repeated tests are required for a reliable performance conclusion.