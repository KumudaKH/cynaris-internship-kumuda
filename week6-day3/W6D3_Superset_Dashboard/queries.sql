-- 1: Bar — employees by department
SELECT department, COUNT(*) AS employees FROM employees GROUP BY department ORDER BY employees DESC, department;

-- 2: Pie — department share
SELECT department, COUNT(*) AS employees FROM employees GROUP BY department;

-- 3: Line — salary by employee ID (not a time series)
SELECT employee_id, salary FROM employees ORDER BY employee_id;

-- 4: KPI — total employees
SELECT COUNT(*) AS total_employees FROM employees;

-- 5: Table — salary summary
SELECT department, COUNT(*) AS employees, ROUND(AVG(salary), 2) AS avg_salary, SUM(salary) AS total_salary FROM employees GROUP BY department ORDER BY department;
