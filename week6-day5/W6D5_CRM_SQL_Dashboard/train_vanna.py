from vanna_setup import get_vanna
from sql_patterns import TRAINING_PAIRS

vn = get_vanna()
for ddl in (
    "CREATE TABLE customers(customer_id INTEGER PRIMARY KEY, name TEXT, region TEXT, industry TEXT);",
    "CREATE TABLE opportunities(opportunity_id INTEGER PRIMARY KEY, customer_id INTEGER, stage TEXT, amount INTEGER, created_date TEXT);"
):
    vn.train(ddl=ddl)
vn.train(documentation="Revenue means amount from opportunities with stage Won only. Amount is INR. Join opportunities.customer_id to customers.customer_id. created_date is an ISO date string.")
for question, sql in TRAINING_PAIRS:
    vn.train(question=question, sql=sql)
    print('Trained:', question)
