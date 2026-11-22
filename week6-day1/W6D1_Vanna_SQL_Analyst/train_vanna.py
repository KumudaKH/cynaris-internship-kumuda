
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

examples = [
    (
        "Show all employees",
        "SELECT * FROM employees"
    ),
    (
        "Show employees working in IT",
        "SELECT * FROM employees WHERE department = 'IT'"
    ),
    (
        "Count the total number of employees",
        "SELECT COUNT(*) AS total FROM employees"
    ),
    (
        "Find the average employee salary",
        "SELECT AVG(salary) AS average_salary FROM employees"
    ),
    (
        "Show the highest paid employee",
        "SELECT * FROM employees ORDER BY salary DESC LIMIT 1"
    )
]

for question, sql in examples:
    vn.train(question=question, sql=sql)
    print("Trained:", question)

print("\nTraining completed successfully!")
