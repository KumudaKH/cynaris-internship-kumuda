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
