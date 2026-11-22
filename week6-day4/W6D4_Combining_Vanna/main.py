"""Local-only demo API. Start with: python -m uvicorn main:app --reload"""
from pathlib import Path
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from query_engine import execute_readonly
from sql_patterns import PAIRS

BASE = Path(__file__).resolve().parent
app = FastAPI(title="W6D4 Executive SQL Reporting")

class Question(BaseModel):
    question: str = Field(min_length=1, max_length=500)

@app.get('/api/summary')
def summary():
    return {
      'department_counts': execute_readonly('SELECT department, COUNT(*) AS count FROM employees GROUP BY department ORDER BY department'),
      'department_salaries': execute_readonly('SELECT department, ROUND(AVG(salary),2) AS average_salary FROM employees GROUP BY department ORDER BY department'),
      'salary_by_employee': execute_readonly('SELECT employee_id, name, salary FROM employees ORDER BY employee_id'),
      'employee_table': execute_readonly('SELECT name, department, city, salary FROM employees ORDER BY employee_id'),
      'metrics': execute_readonly('SELECT COUNT(*) AS employees, SUM(salary) AS monthly_payroll, ROUND(AVG(salary),2) AS average_salary FROM employees')[0]
    }

@app.post('/cia/sql-analyst')
def sql_analyst(payload: Question):
    try:
        from vanna_setup import get_vanna
        sql = get_vanna().generate_sql(question=payload.question, allow_llm_to_see_data=False)
        if not sql:
            raise ValueError('No SQL was generated')
        results = execute_readonly(sql)
        return {'status':'success','question':payload.question,'generated_sql':sql,'row_count':len(results),'results':results}
    except (ValueError, sqlite3.Error) as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=503, detail='Local Vanna/Ollama unavailable or SQL generation failed; check server logs') from exc

app.mount('/', StaticFiles(directory=str(BASE), html=True), name='static')
