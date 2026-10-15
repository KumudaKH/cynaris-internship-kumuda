-- SQL SUBQUERIES & CTEs
-- Week 1 - Day 4

CREATE TABLE sales2 (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    region TEXT NOT NULL,
    product_name TEXT NOT NULL,
    sales REAL NOT NULL
);


INSERT INTO sales2
    (employee_id, employee_name, region, product_name, sales)
VALUES
    (1, 'Amit',   'South', 'Laptop',  75000),
    (2, 'Priya',  'South', 'Mobile',  45000),
    (3, 'Rahul',  'South', 'Tablet',  60000),
    (4, 'Sneha',  'North', 'Laptop',  90000),
    (5, 'Arjun',  'North', 'Mobile',  55000),
    (6, 'Kavya',  'North', 'Tablet',  70000),
    (7, 'Rohit',  'West',  'Laptop',  85000),
    (8, 'Neha',   'West',  'Mobile',  40000),
    (9, 'Kiran',  'West',  'Tablet',  65000),
    (10, 'Ananya','East',  'Laptop',  80000),
    (11, 'Vikram','East',  'Mobile',  50000),
    (12, 'Meera', 'East',  'Tablet',  60000);

select * from sales2;

-- TASK 1: NON-CORRELATED SUBQUERY
-- Find employees whose sales exceed average sales.
SELECT
    employee_name,
    region,
    product_name,
    sales
FROM sales2
WHERE sales > (
    SELECT AVG(sales)
    FROM sales2
)
ORDER BY sales DESC;

-- TASK 2: CORRELATED SUBQUERY
-- Find the top sales performer in each region.
SELECT
    s1.employee_name,
    s1.region,
    s1.product_name,
    s1.sales
FROM sales2 AS s1
WHERE s1.sales = (
    SELECT MAX(s2.sales)
    FROM sales2 AS s2
    WHERE s2.region = s1.region
)
ORDER BY s1.region;

-- TASK 3: REWRITE A NESTED SUBQUERY USING A CTE
-- Find employees whose sales exceed average sales.
WITH average_sales AS (
    SELECT AVG(sales) AS avg_sales
    FROM sales2
)
SELECT
    s.employee_name,
    s.region,
    s.sales
FROM sales2 AS s
CROSS JOIN average_sales AS a
WHERE s.sales > a.avg_sales
ORDER BY s.sales DESC;

-- TASK 4: CHAIN TWO CTEs
-- First calculate regional sales totals.
-- Then calculate the average regional sales total.
-- Finally find regions above that average.
WITH regional_sales AS (
    SELECT
        region,
        SUM(sales) AS total_sales
    FROM sales2
    GROUP BY region
),
average_regional_sales AS (
    SELECT
        AVG(total_sales) AS avg_regional_sales
    FROM regional_sales
)
SELECT
    rs.region,
    rs.total_sales,
    ars.avg_regional_sales
FROM regional_sales AS rs
CROSS JOIN average_regional_sales AS ars
WHERE rs.total_sales > ars.avg_regional_sales
ORDER BY rs.total_sales DESC;

-- STRETCH GOAL
-- Use EXISTS to find regions containing at least one
-- employee with sales greater than 80000.
SELECT DISTINCT s1.region
FROM sales2 AS s1
WHERE EXISTS (
    SELECT 1
    FROM sales2 AS s2
    WHERE s2.region = s1.region
      AND s2.sales > 80000
)
ORDER BY s1.region;


