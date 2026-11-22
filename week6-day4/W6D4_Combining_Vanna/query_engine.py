from pathlib import Path
import sqlite3
import re
DB = Path(__file__).resolve().parent / "company.db"

def execute_readonly(sql, max_rows=100):
    sql = sql.strip()
    # Conservative local demo gate; not a production SQL security boundary.
    if not re.match(r"^SELECT\b", sql, flags=re.I) or ";" in sql.rstrip(";"):
        raise ValueError("Only a single SELECT statement is supported")
    uri = DB.resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as con:
        con.execute("PRAGMA query_only=ON")
        cursor = con.execute(sql)
        cols = [c[0] for c in cursor.description]
        rows = cursor.fetchmany(max_rows + 1)
        if len(rows) > max_rows:
            raise ValueError("Result exceeds row limit")
        return [dict(zip(cols, row)) for row in rows]
