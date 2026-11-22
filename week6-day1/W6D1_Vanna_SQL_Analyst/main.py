
import re
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from vanna_setup import get_vanna

app = FastAPI(
    title="Cynaris CIA SQL Analyst",
    description="Natural Language to SQL using Vanna, Ollama and SQLite",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent

class SQLRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)

# Load the trained Vanna model once
vn = get_vanna()

@app.get("/")
def home():
    return {
        "message": "Cynaris CIA SQL Analyst API is running",
        "status": "success"
    }

@app.post("/cia/sql-analyst")
def sql_analyst(request: SQLRequest):
    try:
        question = request.question

        # Generate SQL using Vanna and Ollama
        sql = vn.generate_sql(
            question=question,
            allow_llm_to_see_data=False
        )

        if not isinstance(sql, str):
            raise ValueError("Vanna did not generate SQL")

        sql = sql.strip()

        # Allow one read-only SELECT statement
        if not re.match(r"^SELECT\b", sql, re.IGNORECASE):
            raise ValueError("Only SELECT queries are allowed")

        if sql.count(";") > 1 or ";" in sql.rstrip(";"):
            raise ValueError("Multiple SQL statements are not allowed")

        # Connect to SQLite in read-only mode
        db_uri = (
            BASE_DIR / "company.db"
        ).as_uri() + "?mode=ro"

        with sqlite3.connect(db_uri, uri=True) as conn:
            conn.execute("PRAGMA query_only = ON")

            cursor = conn.execute(sql)
            columns = [
                column[0] for column in cursor.description
            ]

            rows = cursor.fetchmany(101)

        if len(rows) > 100:
            raise ValueError("Result exceeds 100 rows")

        results = [
            dict(zip(columns, row))
            for row in rows
        ]

        return {
            "status": "success",
            "question": question,
            "generated_sql": sql,
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
            detail="SQL analysis failed"
        )
