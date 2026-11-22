# W6D5 — CRM Natural Language SQL Dashboard

Cynaris Data Analyst Internship · Kumuda KH · Week 6 Day 5

## What's included
- `crm.db`: 50 synthetic customers, 80 synthetic opportunities.
- `dashboard.html`: offline dashboard with bar, pie, line, KPI and table; open in a browser without installation.
- `queries.sql`: 10 reference queries.
- `vanna_setup.py`, `train_vanna.py`: Vanna + Ollama with five CRM training pairs.
- `test_queries.py`: generates and compares ten natural-language SQL queries against reference SQL; saves `test_results.csv`.
- `main.py`: `POST /cia/sql-analyst` FastAPI endpoint.

## Run
1. Open `dashboard.html` in a browser (no dependencies).
2. For NL-to-SQL, install dependencies with `python -m pip install -r requirements.txt`. Ensure Ollama is running and `ollama pull llama3.2` has been completed (or change the model name).
3. Run `python train_vanna.py`, `python test_queries.py`, then `python -m uvicorn main:app --reload`.
4. Test the endpoint at `http://127.0.0.1:8000/docs` with `{ "question": "How many customers are there?" }`.

## Validation and limitations
- Reference SQL was executed against the included synthetic database and saved in `reference_results.csv`.
- The `test_results.csv` is **not prefilled**; it is generated only when local Vanna/Ollama testing runs.
- API and Vanna-generated SQL require local dependencies and have **not been tested here**.
- SQL checking is a demonstration safeguard, **not production-grade security**. Do not expose the API publicly.
- The dashboard is **not Apache Superset** and is not connected live to Vanna; it visualizes a snapshot of the same CRM database.
- Complete two CIA reviews before committing, collect evidence and feedback, and document actual results honestly.
