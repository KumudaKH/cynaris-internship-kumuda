
from vanna_setup import get_vanna

vn = get_vanna()

vn.train(ddl="""
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    city TEXT NOT NULL
);
""")

vn.train(documentation="""
Business rules:
- Salary values are monthly salaries in INR.
- Department names include IT, HR, Finance and Sales.
- Higher salary means a larger numeric salary value.
- Bangalore refers to the city stored as 'Bangalore'.
- Department-wise analysis should use GROUP BY department.
- Highest-paid employees should be ordered by salary DESC.
""")

examples = [
    (
        "Which department has the highest average salary?",
        """
        SELECT department, AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department
        ORDER BY avg_salary DESC
        LIMIT 1
        """
    ),
    (
        "Show total monthly salary expense by department",
        """
        SELECT department, SUM(salary) AS total_salary
        FROM employees
        GROUP BY department
        ORDER BY total_salary DESC
        """
    ),
    (
        "How many employees in each city earn above 40000?",
        """
        SELECT city, COUNT(*) AS employee_count
        FROM employees
        WHERE salary > 40000
        GROUP BY city
        ORDER BY city
        """
    ),
    (
        "Show employees earning above their department average",
        """
        SELECT e.name, e.department, e.salary
        FROM employees e
        WHERE e.salary > (
            SELECT AVG(e2.salary)
            FROM employees e2
            WHERE e2.department = e.department
        )
        ORDER BY e.salary DESC
        """
    ),
    (
        "Which departments have at least 2 employees?",
        """
        SELECT department, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
        HAVING COUNT(*) >= 2
        ORDER BY department
        """
    )
]

for number, (question, sql) in enumerate(examples, 1):
    vn.train(question=question, sql=sql)
    print(f"Trained pattern {number}: {question}")

print("W6D2 custom SQL training completed!")
