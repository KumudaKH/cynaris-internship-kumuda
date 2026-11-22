from pathlib import Path
import sqlite3
import sqlparse

DB_PATH = Path(__file__).resolve().parent / 'crm.db'

def run_select(sql):
    statements = sqlparse.parse(sql)
    if len(statements) != 1 or statements[0].get_type() != 'SELECT':
        raise ValueError('Only a single SELECT query is allowed')
    uri = DB_PATH.resolve().as_uri() + '?mode=ro'
    with sqlite3.connect(uri, uri=True) as conn:
        conn.execute('PRAGMA query_only=ON')
        cur = conn.execute(sql)
        columns = [c[0] for c in cur.description]
        rows = cur.fetchmany(101)
        if len(rows) > 100:
            raise ValueError('Result exceeds 100 rows')
        return [dict(zip(columns, r)) for r in rows]
