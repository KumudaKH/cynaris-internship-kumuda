-- Executive dashboard SQL for SQLite
SELECT department, COUNT(*) AS count FROM employees GROUP BY department ORDER BY department;
SELECT department, ROUND(AVG(salary),2) AS average_salary FROM employees GROUP BY department ORDER BY department;
SELECT employee_id, name, salary FROM employees ORDER BY employee_id;
SELECT COUNT(*) AS employees, SUM(salary) AS monthly_payroll, ROUND(AVG(salary),2) AS average_salary FROM employees;
SELECT name, department, city, salary FROM employees ORDER BY employee_id;
