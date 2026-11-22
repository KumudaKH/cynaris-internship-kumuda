# W6D4 — Executive Employee Reporting (Vanna + lightweight dashboard)

**Intern:** Kumuda KH | **Branch:** `feat/w6d4-3m-kumuda`

## What is included
- Five executive visualizations: bar, pie, line, KPI metrics, employee table (the KPI group is one visualization type).
- Ten-row SQLite dataset, five custom training pairs, ten SQL test cases, FastAPI endpoint `POST /cia/sql-analyst`.
- `dashboard.html` works **offline** with embedded sample data, without installing anything.
- FastAPI `/api/summary` returns real SQLite aggregates; `/cia/sql-analyst` requires Vanna + Ollama.

## Lightweight offline preview (no installs)
Double-click `dashboard.html`. All five visualizations render from embedded sample data. **The AI question box does not work offline.**

## API setup (only if Python dependencies already installed)
1. `python database.py`
2. `python test_queries.py` — verifies 10 **reference SQL queries**, not Vanna generation.
3. Ensure local Ollama is installed/running with model `llama3.2` (`ollama list`). Adjust `vanna_setup.py` if needed.
4. `python train_vanna.py` — trains 5 question/SQL pairs.
5. `python test_queries.py --vanna` — tests generated SQL against reference results; manually inspect SQL for semantics.
6. `python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000`
7. Open `http://127.0.0.1:8000/dashboard.html` or `http://127.0.0.1:8000/docs`.

If dependencies are missing, `pip install -r requirements.txt` is needed and may consume significant storage. Vanna legacy version and Ollama local model are not bundled.

## Limitations and assignment gap
**This is NOT Apache Superset**. No Superset deployment, data source connection, or dashboard export has been performed. Use an actual Superset environment to satisfy the named integration requirement. No colleague feedback or CIA interactions have been performed by this ZIP; complete them and save genuine evidence before claiming completion. Basic SELECT filtering and SQLite read-only access are a local demo only, not production SQL sandboxing.

## Evidence and review
- `evidence/` includes a README placeholder, not fabricated screenshots.
- Save your own screenshots after running the project.
- Obtain two CIA mentor reviews before commits, then create at least two commits, rebase on upstream/main when safe, and push the W6D4 branch.

## Expected sample metrics
10 employees; total monthly payroll ₹439,000; average salary ₹43,900; Finance highest average salary ₹55,000.
