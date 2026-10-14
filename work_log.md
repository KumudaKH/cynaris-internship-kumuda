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

