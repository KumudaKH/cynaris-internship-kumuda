import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from vanna_setup import get_vanna
from query_engine import run_select

app = FastAPI(title='W6D5 CRM NL-to-SQL Analyst')
vn = get_vanna()

class Question(BaseModel):
    question: str = Field(min_length=1, max_length=500)

@app.get('/')
def home():
    return {'status': 'running', 'project': 'W6D5 CRM SQL Dashboard'}

@app.post('/cia/sql-analyst')
def sql_analyst(body: Question):
    try:
        sql = vn.generate_sql(question=body.question, allow_llm_to_see_data=False)
        if not sql:
            raise ValueError('No SQL generated')
        rows = run_select(sql)
        return {'status': 'success', 'question': body.question, 'generated_sql': sql, 'row_count': len(rows), 'results': rows}
    except (ValueError, sqlite3.Error) as e:
        raise HTTPException(status_code=400, detail=str(e))
