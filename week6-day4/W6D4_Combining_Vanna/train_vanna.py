from vanna_setup import get_vanna
from sql_patterns import PAIRS
vn = get_vanna()
vn.train(ddl="CREATE TABLE employees (employee_id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary INTEGER, city TEXT)")
vn.train(documentation="Salaries are monthly INR. Bangalore is stored as 'Bangalore'. Use read-only SELECT queries. Employee IDs are not dates.")
for question, sql in PAIRS:
    vn.train(question=question, sql=sql)
    print("Trained:", question)
print("Five SQL pairs trained successfully")
