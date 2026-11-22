PAIRS = [
("How many employees work in each department?", "SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department ORDER BY department"),
("What is the average salary by department?", "SELECT department, ROUND(AVG(salary), 2) AS average_salary FROM employees GROUP BY department ORDER BY department"),
("What is the total monthly payroll?", "SELECT SUM(salary) AS total_payroll FROM employees"),
("Who are the three highest paid employees?", "SELECT name, department, salary FROM employees ORDER BY salary DESC, name LIMIT 3"),
("Which department has the highest average salary?", "SELECT department, ROUND(AVG(salary),2) AS average_salary FROM employees GROUP BY department ORDER BY average_salary DESC LIMIT 1")
]
TESTS = PAIRS + [
("How many employees are in Bangalore?", "SELECT COUNT(*) AS employee_count FROM employees WHERE city = 'Bangalore'"),
("What is the minimum salary?", "SELECT MIN(salary) AS minimum_salary FROM employees"),
("What is the average salary of IT employees?", "SELECT AVG(salary) AS average_salary FROM employees WHERE department = 'IT'"),
("How many employees work in each city?", "SELECT city, COUNT(*) AS employee_count FROM employees GROUP BY city ORDER BY city"),
("Which employees earn above 40000?", "SELECT name, salary FROM employees WHERE salary > 40000 ORDER BY salary DESC, name")
]
