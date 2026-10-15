## DAY -1
### CIA Activity — Common SQL Mistakes for Junior Data Analysts

**Question asked:**
What are the most common SQL mistakes junior data analysts make?

**Key Insights Learned:**

CIA explained common SQL mistakes that junior data analysts should avoid when writing queries.

1. **Selecting unnecessary columns:** Avoid using `SELECT *` when only specific columns are required.
2. **Missing WHERE clauses:** Always check whether filtering conditions are necessary to avoid retrieving unintended records.
3. **Incorrect comparison operators:** Use appropriate SQL operators such as `=`, `<>`, `>`, `<`, `>=`, and `<=`.
4. **Incorrect string quoting:** Use single quotes for string values, such as `WHERE city = 'Bengaluru'`.
5. **Incorrect NULL handling:** Use `IS NULL` or `IS NOT NULL` instead of comparing values with `= NULL`.
6. **Datatype mismatches:** Ensure comparisons use compatible data types.
7. **Incorrect logical conditions:** Use parentheses when combining `AND` and `OR` to ensure the intended filtering logic.
8. **Missing aliases:** Use table and column aliases to improve query readability.
9. **Retrieving excessive records:** Use `LIMIT` when exploring large datasets.
10. **Incorrect date formats:** Use appropriate date formats and database-specific date handling.
11. **Incorrect JOIN conditions:** Use explicit JOIN syntax and appropriate matching conditions to avoid unintended Cartesian products.
12. **Ignoring performance:** Examine query execution plans and consider indexes when working with large datasets.
13. **Poor documentation:** Add comments to explain complex query logic.

**Practical Learning:**

Learned the importance of writing accurate, readable, and efficient SQL queries by selecting only necessary columns, applying appropriate filters, handling NULL values correctly, and using proper JOIN conditions.

**Application in Data Analytics:**

These practices help improve data accuracy, query readability, and performance when preparing reports and analysing business data.

**Status:** CIA insights documented.
______________________________________________________________________


## DAY 2
### CIA Activity — Difference Between INNER JOIN and LEFT JOIN

**Question asked:**
Explain the difference between LEFT JOIN and INNER JOIN with a business reporting example.

**Key Insights Learned:**

CIA explained how INNER JOIN and LEFT JOIN combine records from related tables.

**1. INNER JOIN**

* Returns only records with matching values in both tables.
* Useful when a report should include only entities with related records.
* Example: Identifying customers who have placed orders.

**2. LEFT JOIN**

* Returns all records from the left table and matching records from the right table.
* If no matching record exists, the right-side columns contain NULL.
* Useful when a report must include every entity, even if related records do not exist.
* Example: Identifying all customers, including those who have never placed an order.

**Business Reporting Example:**

In an e-commerce company, customer information may be stored in a `customers` table, while purchase details are stored in an `orders` table.

An INNER JOIN can identify customers who have placed orders, helping analysts study purchasing behaviour.

A LEFT JOIN can display every customer, including customers without orders. Using `COUNT()` and `COALESCE()`, analysts can identify customers with zero orders and zero spending.

**Example SQL Query — INNER JOIN:**

```sql
SELECT
    c.cust_id,
    c.cust_name,
    SUM(o.order_amt) AS total_spent
FROM customers AS c
INNER JOIN orders AS o
    ON c.cust_id = o.cust_id
GROUP BY c.cust_id, c.cust_name;
```

**Example SQL Query — LEFT JOIN:**

```sql
SELECT
    c.cust_id,
    c.cust_name,
    COUNT(o.order_id) AS orders_count,
    COALESCE(SUM(o.order_amt), 0) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o
    ON c.cust_id = o.cust_id
GROUP BY c.cust_id, c.cust_name;
```

**Important Difference:**

* INNER JOIN excludes customers without matching orders.
* LEFT JOIN retains all customers, including those without matching orders.
* `COUNT(o.order_id)` returns zero for customers without orders.
* `COALESCE(SUM(o.order_amt), 0)` displays zero instead of NULL when no order amounts exist.

**Business Application:**

INNER JOIN is useful for analysing customers with purchases, while LEFT JOIN helps identify inactive customers for marketing and customer re-engagement campaigns.

**Status:** CIA insights documented.
______________________________________________________________________

## DAY -3 
5 Retail‑Business KPIs You Can Derive with SQL GROUP BY
#	KPI	What it tells the business	Typical tables/columns	Sample GROUP BY query
1. Total Sales Revenue	Overall topline; helps set targets and compare periods.	sales (sale_id, sale_date, store_id, product_id, qty, unit_price)	sql\nSELECT DATE_TRUNC('month', sale_date) AS month,\n SUM(qty * unit_price) AS revenue\nFROM sales\nGROUP BY month\nORDER BY month;

2. Average Transaction Value (ATV)	Avg amount per receipt – indicator of upselling effectiveness.	sales (sale_id, sale_date, receipt_no, qty, unit_price)	sql\nSELECT DATE_TRUNC('day', sale_date) AS day,\n AVG(qty * unit_price) AS avg_txn_value\nFROM sales\nGROUP BY day\nORDER BY day;

3. Units Sold per Product Category	Spot‑light top‑selling categories & inventory needs.	sales + products (product_id, category)	sql\nSELECT p.category,\n SUM(s.qty) AS units_sold\nFROM sales s\nJOIN products p ON s.product_id = p.product_id\nGROUP BY p.category\nORDER BY units_sold DESC;

4. Store‑wise Gross Margin %	Profitability per outlet; helps decide store expansions/closures.	sales, products (product_id, cost_price)	sql\nSELECT s.store_id,\n (SUM(s.qty * (s.unit_price - p.cost_price)) /\n SUM(s.qty * s.unit_price)) * 100 AS gross_margin_pct\nFROM sales s\nJOIN products p ON s.product_id = p.product_id\nGROUP BY s.store_id\nORDER BY gross_margin_pct DESC;

5. Repeat‑Customer Rate	Share of customers who bought more than once – a loyalty health metric.	sales (sale_id, sale_date, customer_id)	sql\nWITH cust_counts AS (\n SELECT customer_id,\n COUNT(DISTINCT sale_id) AS txn_cnt\n FROM sales\n GROUP BY customer_id\n)\nSELECT ROUND(100.0 * SUM(CASE WHEN txn_cnt > 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS repeat_customer_pct\nFROM cust_counts;

Quick tips for implementation
Date granularity – use DATE_TRUNC('day'|'month'|'quarter') (PostgreSQL) or DATE_FORMAT(...,'%Y-%m') (MySQL) to roll‑up time.
Performance – add indexes on the columns used in the GROUP BY (e.g., sale_date, store_id, product_id).
Null safety – wrap calculations with COALESCE(...,0) if any cost/price fields may be NULL.
These five KPIs give a solid snapshot of revenue health, customer behavior, product performance, and store profitability—exactly the kind of metrics a Data Analyst Intern at an Indian retail firm (e.g., Big Bazaar, Reliance Retail, or a regional grocery chain) would be expected to produce. 

______________________________________________________________________

## DAY - 4
# CTE vs Subquery – When to Use Which & What the Performance Impact Is

| Aspect                                         | **Common Table Expression (CTE)**                                                                                                                                                                                                                                                                                                                         | **Inline Subquery**                                                                                                                                                                                                             |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Syntax & readability**                       | `WITH cte_name AS (...) SELECT ... FROM cte_name` – separates the logic from the main query, making complex pipelines easier to read and debug.                                                                                                                                                                                                           | `SELECT ... FROM (SELECT ... FROM ...) AS t` – nests the query inside the `FROM` clause; can become hard to follow when you have many layers.                                                                                   |
| **Reusability within the same statement**      | Can be referenced **multiple times** in the outer query or in other CTEs.                                                                                                                                                                                                                                                                                 | Must repeat the subquery each time you need it, or wrap it in a derived table and join again.                                                                                                                                   |
| **Recursion**                                  | Only CTEs support **recursive** definitions (`WITH RECURSIVE ...`).                                                                                                                                                                                                                                                                                       | Subqueries cannot be recursive.                                                                                                                                                                                                 |
| **Materialization (how the engine treats it)** | *Implementation-dependent:* PostgreSQL 13+ and SQL Server usually inline CTEs (the optimizer expands them like a subquery). Oracle materializes them once unless the `/*+ MATERIALIZE */` or `/*+ INLINE */` hint is used.                                                                                                                                | Treated as a derived table that the optimizer may materialize or push down predicates. Most modern engines try to flatten it, but if it is large, it might be materialized temporarily.                                         |
| **Performance-wise**                           | In most DBMS (SQL Server, PostgreSQL, MySQL 8+, Snowflake), there is no penalty because the optimizer rewrites the CTE into the main plan. When a CTE is referenced multiple times, the optimizer may compute it once (materialize), which can save work if the CTE is expensive or cause a single-pass bottleneck if it returns a huge intermediate set. | Inline subqueries are flattened when possible, allowing the optimizer to push predicates down and avoid materialization. If the subquery is correlated, it may be executed repeatedly (row by row), which can hurt performance. |
| **When the optimizer can push predicates**     | Good for **filter pushdown** if the CTE is simple. Complex CTEs that reference many tables may limit pushdown, especially on older engines.                                                                                                                                                                                                               | The optimizer can push predicates into the derived table if possible, but a correlated subquery may limit this.                                                                                                                 |
| **Memory footprint**                           | If materialized, it occupies temporary space equal to the CTE result size.                                                                                                                                                                                                                                                                                | The same applies to a materialized derived table; otherwise, it is streamed.                                                                                                                                                    |

---

## Practical Decision

| Situation                                                               | Prefer **CTE**                                                                                                                                                   | Prefer **Subquery**                                                      |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Readability of a long query**                                         | Use a CTE – each logical step gets its own name.                                                                                                                 | Inline subqueries can become a wall of parentheses.                      |
| **Need the same intermediate result in 2+ places**                      | Write the CTE once and reference it multiple times.                                                                                                              | You would have to duplicate the subquery or create a temporary table.    |
| **Recursive hierarchy (e.g., bill of materials, organizational chart)** | `WITH RECURSIVE ...` is the only option.                                                                                                                         | Not possible.                                                            |
| **Very large intermediate result that you do not need more than once**  | Might cause a costly materialization step. Use a subquery or temporary table to let the optimizer stream rows.                                                   | An inline subquery encourages the optimizer to stream rather than store. |
| **You need predicate pushdown on a simple filter**                      | Works fine if the CTE is simple.                                                                                                                                 | Also works, but the optimizer will often inline automatically.           |
| **Database engine specifics**                                           | SQL Server, PostgreSQL, and Snowflake usually inline CTEs, resulting in no performance hit. Oracle may materialize CTEs by default, so check the execution plan. | Works similarly across engines; still watch for correlated subqueries.   |
| **Testing / debugging**                                                 | You can run the CTE alone (`WITH ... SELECT * FROM cte_name`) to inspect intermediate data.                                                                      | Harder to test without creating a temporary table.                       |

---

## Quick Cheat Sheet for Common Database Engines

| DBMS                  | CTE Handling                                                             | Subquery Handling                                                     |
| --------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **SQL Server**        | Inlined, except when `OPTION (MAXRECURSION...)` or explicit hints apply. | Inlined; correlated subqueries may be executed per row.               |
| **PostgreSQL (v13+)** | Inlined unless you use the `MATERIALIZED` keyword.                       | Inlined; same predicate pushdown rules.                               |
| **MySQL 8+**          | Treated like a derived table; the optimizer often merges it.             | Inlined; correlated subqueries can be costly.                         |
| **Oracle**            | Materialized by default; use `/*+ INLINE */` to force inlining.          | Inlined when possible; materialization may be used for complex joins. |
| **Snowflake**         | Inlined; a CTE is primarily a naming convenience.                        | Same as CTE.                                                          |

---

## TL;DR

* **Use a CTE** when you value readability, need recursion, or must reuse an intermediate result multiple times.
* **Use an inline subquery** or a derived table when the intermediate result is large and used only once, or when you are on a platform such as Oracle where CTEs default to materialization and you want to avoid extra temporary storage.
* **Always check the execution plan** (`EXPLAIN`, `SET SHOWPLAN_ALL`, etc.) after writing a query. This tells you whether the engine materialized the CTE or flattened the subquery, allowing you to adjust with hints (`INLINE`, `MATERIALIZE`) or by refactoring.

___________________________________________________________________________________________________________

# Week 1, Day 5 — Python Pandas Basics

## 1. Task

Exploratory Data Analysis (EDA) using Python Pandas.

## 2. CIA Research Query

**Question:** What are the most useful Pandas methods for exploratory data analysis?

## 3. Key Learnings

I learned that Pandas provides several useful methods for quickly understanding, cleaning, and analysing datasets.

* **Dataset inspection:** `head()`, `tail()`, `shape`, and `info()` help understand the dataset's structure, dimensions, and column data types.
* **Statistical analysis:** `describe()` provides summary statistics such as mean, standard deviation, minimum, and maximum.
* **Missing-value detection:** `isnull().sum()` identifies missing values in each column.
* **Categorical analysis:** `value_counts()` and `nunique()` help identify category frequencies and unique values.
* **Data filtering:** Boolean indexing helps extract rows that meet specific conditions.
* **Grouping and aggregation:** `groupby()` and `agg()` summarise data by categories.
* **Sorting:** `sort_values()` arranges records based on selected columns.
* **Correlation analysis:** `corr()` helps examine relationships between numerical variables.
* **Pivot tables:** `pivot_table()` summarises data across multiple dimensions.
* **Visualisation:** `hist()` and `boxplot()` help examine distributions and potential outliers.

## 4. Practical Application

I applied Pandas concepts to an employee mental health and burnout dataset. The workflow included loading a CSV file, inspecting its structure, identifying missing values, filtering records, grouping data, calculating aggregate statistics, and exporting cleaned data.

## 5. Important Code Examples

```python
# Inspect the dataset
print(df.shape)
print(df.head())
df.info()

# Summary statistics
print(df.describe())

# Identify missing values
print(df.isnull().sum())

# Count categorical values
print(df["gender"].value_counts())

# Group and aggregate data
print(
    df.groupby("job_role").agg(
        Average_Stress=("stress_level", "mean"),
        Average_Burnout=("burnout_score", "mean")
    )
)


## 6. Key Takeaway

Pandas simplifies exploratory data analysis by providing methods to inspect, clean, filter, group, and summarise data efficiently. These skills are useful for identifying data-quality issues, understanding patterns, and preparing datasets for further analysis.
