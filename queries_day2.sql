-- Cynaris Internship
-- Week 1 Day 2: SQL Joins
-- Objective: Demonstrate INNER, LEFT, RIGHT, and FULL OUTER JOINs,
-- duplicate rows, self-joins, and table aliases.

CREATE TABLE employees (
employee_id INTEGER PRIMARY KEY,
employee_name TEXT NOT NULL,
department_id INTEGER
);

CREATE TABLE departments (
department_id INTEGER PRIMARY KEY,
department_name TEXT NOT NULL
);

-- Insert employee records
INSERT INTO employees VALUES (1, 'Kumuda', 101);
INSERT INTO employees VALUES (2, 'Kusuma', 102);
INSERT INTO employees VALUES (3, 'Darshini', 103);
INSERT INTO employees VALUES (4, 'Bhoomika', 103);
INSERT INTO employees VALUES (5, 'Manjesh', NULL);

-- Insert department records
INSERT INTO departments VALUES (101, 'IT');
INSERT INTO departments VALUES (102, 'HR');
INSERT INTO departments VALUES (104, 'Finance');

select * 
from employees;

select * 
from departments;

-- 1. INNER JOIN
SELECT
e.employee_id,
e.employee_name,
d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id;

-- 2. LEFT JOIN
SELECT
e.employee_id,
e.employee_name,
d.department_name
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id;

-- RIGHT JOIN 
SELECT
e.employee_name,
d.department_name
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id;

-- FULL JOIN
SELECT
e.employee_id,
e.employee_name,
d.department_name
FROM employees AS e
FULL OUTER JOIN departments AS d
ON e.department_id = d.department_id;

-- UNDERSTAND DUPLICATE ROWS 
CREATE TABLE employee_assignments (
assignment_id INTEGER PRIMARY KEY,
employee_id INTEGER,
project_name TEXT
);

INSERT INTO employee_assignments VALUES (1, 1, 'Website');
INSERT INTO employee_assignments VALUES (2, 1, 'Database');
INSERT INTO employee_assignments VALUES (3, 2, 'Website');

SELECT
e.employee_name,
a.project_name
FROM employees AS e
INNER JOIN employee_assignments AS a
ON e.employee_id = a.employee_id;

SELECT
e.employee_id,
e.employee_name,
COUNT (a.assignment_id) AS assignment_count
FROM employees AS e
LEFT JOIN employee_assignments AS a
ON e.employee_id = a.employee_id
GROUP BY e.employee_id, e.employee_name;

-- DISTINCT removes identical result rows when appropriate
SELECT DISTINCT
e.employee_name
FROM employees AS e
INNER JOIN employee_assignments AS a
ON e.employee_id = a.employee_id;

-- SELF-JOIN
-- employees who belong to the same department
SELECT
e1.employee_name AS employee_one,
e2.employee_name AS employee_two,
e1.department_id
FROM employees AS e1
INNER JOIN employees AS e2
ON e1.department_id = e2.department_id
AND e1.employee_id < e2.employee_id;

--- TABLE ALIASES
SELECT
e.employee_name AS employee,
d.department_name AS department
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id;


