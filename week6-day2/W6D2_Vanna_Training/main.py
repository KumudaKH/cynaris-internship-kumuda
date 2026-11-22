
from pathlib import Path
import re
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from vanna_setup import get_vanna

app = FastAPI(
    title="W6D2 Vanna SQL Analyst",
    description="Natural Language to SQL using Vanna, Ollama and SQLite",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "company.db"

vn = get_vanna()


class SQLRequest(BaseModel):
    question: str = Field(min_length=1)


@app.get("/")
def home():
    return {
        "message": "W6D2 Vanna SQL Analyst API",
        "status": "running"
    }


def execute_sql(sql):
    sql = sql.strip()

    # Basic validation for the local internship demo.
    if not re.match(r"^SELECT\b", sql, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed")

    if ";" in sql.rstrip(";"):
        raise ValueError("Multiple SQL statements are not allowed")

    db_uri = DB_PATH.resolve().as_uri() + "?mode=ro"

    with sqlite3.connect(db_uri, uri=True) as conn:
        conn.execute("PRAGMA query_only = ON")

        cursor = conn.execute(sql)
        columns = [item[0] for item in cursor.description]

        rows = cursor.fetchmany(101)

        if len(rows) > 100:
            raise ValueError("Query returned more than 100 rows")

        return [
            dict(zip(columns, row))
            for row in rows
        ]


@app.post("/cia/sql-analyst")
def sql_analyst(request: SQLRequest):
    try:
        generated_sql = vn.generate_sql(
            question=request.question,
            allow_llm_to_see_data=False
        )

        if not generated_sql:
            raise ValueError("Vanna did not generate SQL")

        results = execute_sql(generated_sql)

        return {
            "status": "success",
            "question": request.question,
            "generated_sql": generated_sql,
            "row_count": len(results),
            "results": results
        }

    except (ValueError, sqlite3.Error) as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="SQL generation or execution failed"
        )
