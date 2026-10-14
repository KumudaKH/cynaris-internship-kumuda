-- Cynaris Internship
-- Week 1 - Day 1
-- SQL Fundamentals: SELECT, FROM, WHERE


CREATE TABLE sales1 (
    sale_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT,
    product TEXT,
    quantity INTEGER,
    amount REAL,
    payment_method TEXT,
    phone TEXT
);


 
 INSERT INTO sales1 VALUES
(1, 'Rahul', 'Bengaluru', 'Laptop', 1, 55000, 'UPI', '9876543210'),
(2, 'Priya', 'Mysuru', 'Mouse', 2, 800, 'Cash', '9876543211'),
(3, 'Amit', 'Bengaluru', 'Keyboard', 1, 1500, 'Card', NULL),
(4, 'Sneha', 'Hubballi', 'Monitor', 1, 12000, 'UPI', '9876543213'),
(5, 'Kiran', 'Mysuru', 'Laptop', 1, 60000, 'Card', '9876543214'),
(6, 'Ananya', 'Bengaluru', 'Mouse', 3, 1200, 'Cash', NULL),
(7, 'Arjun', 'Pune', 'Keyboard', 2, 3000, 'UPI', '9876543216'),
(8, 'Meera', 'Hubballi', 'Laptop', 1, 52000, 'Card', '9876543217'),
(9, 'Vikram', 'Pune', 'Monitor', 2, 24000, 'UPI', '9876543218'),
(10, 'Divya', 'Mysuru', 'Mouse', 1, 400, 'Cash', '9876543219');

-- 1. Display all records
SELECT *
FROM sales1;

-- 2. Select specific columns
select customer_name, city, amount
from sales1;

-- 3. Filter sales from Bengaluru
select *
from sales1
where city = 'Bengaluru';

-- 4. Use AND
select * 
from sales1
where city = 'Bengaluru'
and amount > 50000;

select * 
from sales1
where city = 'Mysuru'
and amount <= 50000;

-- 5. use OR
SELECT *
FROM sales1
WHERE city = 'Bengaluru'
OR city = 'Mysuru';

-- 6. use NOT
select *
from sales1
where not city = 'Bengaluru';

-- 7. use LIKE
select *
from sales1
where customer_name like 'A%';

-- 8. use IN
select * 
from sales1
where city in  ('Bengaluru','Mysuru');

-- 9. use BETWEEN
select * 
from sales1
where amount BETWEEN 1000 and 2000;

-- 10.use IS NULL
select *
from sales1
where phone is NULL;

select customer_name, city,product,amount
from sales1
where amount >10000;


select count(*) as total_records
from sales1;

