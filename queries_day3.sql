-- SQL Aggregations — GROUP BY & HAVING
-- Day 3 | Week 1
-- SQL AGGREGATIONS: GROUP BY & HAVING

CREATE TABLE sales (
sale_id INTEGER PRIMARY KEY,
sale_date DATE NOT NULL,
region TEXT NOT NULL,
category TEXT NOT NULL,
product_name TEXT NOT NULL,
quantity INTEGER NOT NULL,
sales_amount REAL NOT NULL
);

INSERT INTO sales
(sale_id, sale_date, region, category, product_name, quantity, sales_amount)
VALUES
(1, '2026-01-05', 'South', 'Electronics', 'Headphones', 2, 2000),
(2, '2026-01-08', 'North', 'Furniture', 'Chair', 3, 4500),
(3, '2026-01-12', 'South', 'Groceries', 'Rice', 10, 1200),
(4, '2026-01-15', 'West', 'Electronics', 'Keyboard', 2, 3000),
(5, '2026-01-20', 'East', 'Furniture', 'Table', 1, 5000),
(6, '2026-02-03', 'South', 'Electronics', 'Monitor', 2, 10000),
(7, '2026-02-07', 'North', 'Groceries', 'Oil', 5, 2500),
(8, '2026-02-11', 'West', 'Furniture', 'Desk', 2, 8000),
(9, '2026-02-14', 'East', 'Electronics', 'Mouse', 4, 2000),
(10, '2026-02-19', 'South', 'Furniture', 'Sofa', 1, 12000),
(11, '2026-03-02', 'North', 'Electronics', 'Laptop', 1, 45000),
(12, '2026-03-06', 'West', 'Groceries', 'Sugar', 10, 800),
(13, '2026-03-10', 'East', 'Furniture', 'Cabinet', 2, 7000),
(14, '2026-03-15', 'South', 'Groceries', 'Wheat', 8, 1600),
(15, '2026-03-20', 'North', 'Electronics', 'Printer', 1, 9000);

SELECT * FROM sales;


-- EIGHT AGGREGATE QUERIES

-- QUERY 1: COUNT
-- Count the total number of sales records.
SELECT
COUNT(*) AS total_sales_records
FROM sales;

-- QUERY 2: SUM
-- Calculate total revenue.
SELECT
SUM(sales_amount) AS total_revenue
FROM sales;

-- QUERY 3: AVG
-- Calculate the average sales amount.
SELECT
AVG(sales_amount) AS average_sales
FROM sales;

-- QUERY 4: MAX AND MIN
-- Find the highest and lowest sale amounts.
SELECT
MAX(sales_amount) AS highest_sale,
MIN(sales_amount) AS lowest_sale
FROM sales;

-- QUERY 5: GROUP BY REGION
-- Calculate total sales for each region.
SELECT
region,
SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- QUERY 6: GROUP BY CATEGORY
-- Calculate total revenue for each category.
SELECT
category,
SUM(sales_amount) AS category_revenue
FROM sales
GROUP BY category
ORDER BY category_revenue DESC;

-- QUERY 7: GROUP BY MONTH
-- Calculate monthly revenue.
SELECT
strftime('%Y-%m', sale_date) AS sales_month,
SUM(sales_amount) AS monthly_revenue
FROM sales
GROUP BY strftime('%Y-%m', sale_date)
ORDER BY sales_month;

-- QUERY 8: GROUP BY AND HAVING
-- Find regions with total sales greater than 10000.
SELECT
region,
SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(sales_amount) > 10000
ORDER BY total_sales DESC;


-- WINDOW FUNCTION

-- QUERY 9: RUNNING TOTAL USING SUM() OVER()
-- Calculate cumulative sales while retaining individual rows.
SELECT
sale_id,
sale_date,
region,
sales_amount,
SUM(sales_amount) OVER (
ORDER BY sale_date, sale_id
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_total
FROM sales
ORDER BY sale_date, sale_id;

