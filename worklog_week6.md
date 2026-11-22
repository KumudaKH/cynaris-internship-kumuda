# Week 6 — Data Analyst Internship Worklog
**Week:** 6  
**Day:** 1  
**Date:** 22 November 2026  
**Task:** Vanna Setup — Natural Language to SQL on Real Database  
**Branch:** `feat/w6d1-3m-kumuda`

---

## Day 1: Vanna Setup — NL to SQL

### Objective

To develop an AI-powered SQL Analyst that converts natural-language questions into SQL queries using Vanna and Ollama, connects to a SQLite database, and exposes the functionality through a FastAPI endpoint.

### Work Completed

1. **Database Setup**
   - Created a SQLite database named `company.db`.
   - Created an `employees` table containing employee ID, name, department, salary, and city.
   - Inserted 10 sample employee records.
   - Verified database connectivity and records using Python.

2. **Vanna and Ollama Integration**
   - Configured Vanna with the locally installed Ollama model.
   - Integrated ChromaDB for storing SQL training examples.
   - Connected Vanna to the SQLite database.
   - Prepared 5 natural-language question–SQL training pairs.

3. **Natural Language to SQL Testing**
   - Implemented 10 natural-language SQL test cases.
   - Added reference SQL queries for correctness verification.
   - Compared generated query results against expected database results.
   - Generated `test_results.csv` for recording test outcomes.

4. **FastAPI Development**
   - Created the `POST /cia/sql-analyst` endpoint.
   - Implemented natural-language question input and SQL generation.
   - Added database query execution and JSON response handling.
   - Included basic read-only SQL validation and exception handling.
   - Prepared API testing through Swagger UI.

5. **GitHub and Documentation**
   - Created the feature branch `feat/w6d1-3m-kumuda`.
   - Pushed the feature branch to GitHub.
   - Prepared project documentation and Pull Request description.
   - Organised an `evidence/` folder for execution screenshots and CIA review records.

### Technologies Used

- Python
- SQLite
- Vanna AI
- Ollama
- ChromaDB
- FastAPI
- Git and GitHub
- Visual Studio Code

### Files Created

| File | Description |
|---|---|
| `database.py` | Creates and populates the SQLite database |
| `vanna_setup.py` | Configures Vanna, Ollama and SQLite |
| `train_vanna.py` | Trains Vanna using 5 question–SQL pairs |
| `test_queries.py` | Tests 10 natural-language queries |
| `main.py` | Implements the CIA SQL Analyst API |
| `test_results.csv` | Stores SQL testing results |
| `evidence/` | Stores screenshots and review evidence |

### Testing and Results

The SQLite database was created with 10 employee records. Vanna training and SQL testing scripts were prepared and run during the practical session.

The expected results include:

- Total employees: 10
- IT department employees: 4
- Average salary: ₹43,900
- Highest salary: ₹60,000
- Minimum salary: ₹32,000

Actual SQL test pass counts and API response evidence are recorded separately in the project files and screenshots.

### Challenges and Solutions

**Challenge 1:** Configuring natural-language-to-SQL generation without a paid cloud API.

**Solution:** Used Ollama as a local language model integrated with Vanna.

**Challenge 2:** Verifying AI-generated SQL correctness.

**Solution:** Created reference SQL queries and compared their database results with the generated queries.

**Challenge 3:** Managing Git commits without affecting previous internship assignments.

**Solution:** Used a dedicated W6D1 feature branch and staged project-specific files.

### Learning Outcomes

- Understood natural-language-to-SQL conversion using Vanna.
- Learned to integrate local LLMs using Ollama.
- Gained practical experience with SQLite database connectivity.
- Practised SQL generation and result verification.
- Learned how to expose AI functionality through FastAPI.
- Improved Git branching, commit and Pull Request workflow.


### GitHub Details

**Repository:** https://github.com/KumudaKH/cynaris-internship-kumuda

**Feature Branch:** `feat/w6d1-3m-kumuda`

**Pull Request:** Add PR URL after creation.

### Day 1 Summary

Worked on an AI-powered SQL Analyst using Vanna, Ollama, SQLite and FastAPI. The project demonstrates how natural-language questions can be translated into SQL queries and executed against a structured database. The implementation includes training examples, automated query verification, an API endpoint and GitHub submission preparation.

**Status:** Implementation completed; final Git and evidence verification pending.
____________________________________________________________________________________________________________

## Day 3 — Wednesday, 18 November 2026

**Topic:** W6D3 — Apache Superset: BI Dashboard from SQL Results

**Hours Worked:** 1 hour (curriculum duration — update to actual hours)

### Work Completed

- Continued the Week 6 SQL Analyst project by working on business intelligence dashboard visualisation.
- Prepared a lightweight, browser-based Employee Analytics Dashboard because of limited laptop storage.
- Used the existing employee dataset containing 10 records across four departments.
- Prepared five dashboard visualisations:
  1. Bar Chart — Employees by Department
  2. Line Chart — Employee Salary Distribution
  3. Pie Chart — Department-wise Employee Distribution
  4. KPI Metric — Total Employees
  5. Table — Department Salary Summary
- Prepared SQL queries for employee count, department distribution and salary analysis.
- Organised the dashboard files, CSV dataset, SQL queries and documentation.
- Prepared dashboard evidence and GitHub submission steps.

### Tools and Technologies Used

HTML, CSS, JavaScript, SQL, SQLite, CSV, VS Code, Git and GitHub.

**Implementation Note:** Used a lightweight HTML dashboard as an alternative to Apache Superset because of local storage limitations. Apache Superset was not installed or deployed.

### Challenges and Solutions

**Challenge 1: Insufficient Laptop Storage**

**Solution:** Prepared a lightweight HTML-based dashboard that can run directly in a browser without Docker or Apache Superset installation.

**Challenge 2: Presenting SQL Results Visually**

**Solution:** Organised employee data into five visualisations to display department distribution, salaries and employee statistics.

**Challenge 3: Completing the Dashboard Assignment**

**Solution:** Prepared the dashboard implementation and documentation. Actual Apache Superset deployment remains incomplete because of the storage constraint.

### Learning Outcomes

- Understood the role of business intelligence dashboards in data analysis.
- Learned how SQL query results can be presented using charts and KPI metrics.
- Gained experience interpreting employee and salary data.
- Understood the importance of dashboard readability and visualisation selection.
- Learned how to organise dashboard deliverables for GitHub submission.

### W6D3 Deliverables

| File | Description |
|---|---|
| `dashboard.html` | Employee Analytics Dashboard |
| `employees.csv` | Employee dataset |
| `queries.sql` | SQL queries for dashboard analysis |
| `README.md` | Project documentation |
| `evidence/` | Dashboard screenshot evidence |

### GitHub Details

**Repository:** https://github.com/KumudaKH/cynaris-internship-kumuda

**Branch:** `feat/w6d3-3m-kumuda`



### Day 3 Summary

Worked on the Employee Analytics BI Dashboard using SQL-based employee data. Prepared five visualisations covering employee distribution, salary analysis and key metrics. Due to limited storage, a lightweight HTML dashboard was used instead of a local Apache Superset installation.

**Status:** Alternative dashboard prepared; final validation, colleague feedback, CIA review and GitHub submission pending.

---

## Week 6 Progress Summary

**Day 1:** Vanna setup, SQLite database connectivity, natural-language-to-SQL generation and FastAPI integration.

**Day 2:** Domain-specific Vanna training, custom SQL patterns, query validation and API testing.

**Day 3:** Employee Analytics BI Dashboard with five visualisations and SQL-based reporting.

**Overall Progress:** W6D1–W6D3 implementation work prepared. Final verification and submission requirements should be completed before marking the practical tasks fully finished.
____________________________________________________________________________________________________________

## Day 4 — Thursday, 19 November 2026

**Topic:** W6D4 — Combining Vanna + Superset for Executive Reporting

**Hours Worked:** 1 hour (curriculum duration — update to actual hours)

### Work Completed

- Continued the Week 6 Natural Language to SQL Analyst project.
- Prepared a lightweight Executive Reporting System using Vanna AI, Ollama, SQLite and FastAPI.
- Organised the employee database and SQL reporting components.
- Prepared 5 question–SQL training examples for natural-language query generation.
- Included 10 SQL test cases for validating database query results.
- Prepared the `POST /cia/sql-analyst` FastAPI endpoint for natural-language SQL analysis.
- Created an HTML-based executive dashboard for presenting employee and salary statistics.
- Included five visualisation types: bar chart, line chart, pie chart, KPI metric and data table.
- Organised the project files, dataset, SQL queries and documentation.

### Tools and Technologies Used

Python, Vanna AI, Ollama, SQLite, SQL, FastAPI, HTML, CSS, JavaScript, Git, GitHub and VS Code.

**Implementation Note:** Due to limited laptop storage, a lightweight HTML dashboard was used instead of installing Apache Superset. Actual Apache Superset integration remains incomplete.

### Challenges and Solutions

**Challenge 1: Limited Laptop Storage**

**Solution:** Used a lightweight HTML dashboard that can run in a browser without Docker or Apache Superset installation.

**Challenge 2: Combining SQL Analysis with Executive Reporting**

**Solution:** Organised Vanna-based SQL generation, database queries and dashboard visualisations into one reporting project.

**Challenge 3: Verifying SQL Query Correctness**

**Solution:** Prepared 10 SQL test cases and reference queries to compare expected database results.

### Testing and Validation

- Prepared 5 Vanna training examples.
- Included 10 SQL test cases.
- Reference SQL tests were executed successfully during project preparation.
- Prepared an offline executive dashboard.
- Vanna-generated SQL and FastAPI end-to-end testing remain pending in the local Ollama environment.

### Learning Outcomes

- Understood how natural-language-to-SQL tools support business reporting.
- Learned how Vanna can generate SQL queries from business questions.
- Gained experience combining database analysis with dashboard visualisations.
- Practised SQL testing and API integration.
- Understood the role of business intelligence dashboards in executive decision-making.

### W6D4 Deliverables

| File | Description |
|---|---|
| `dashboard.html` | Executive reporting dashboard |
| `company.db` | SQLite employee database |
| `employees.csv` | Employee dataset |
| `vanna_setup.py` | Vanna and Ollama configuration |
| `train_vanna.py` | Five SQL training examples |
| `test_queries.py` | Ten SQL test cases |
| `test_results.csv` | SQL test results |
| `main.py` | FastAPI SQL Analyst endpoint |
| `queries.sql` | SQL reporting queries |
| `README.md` | Project documentation |
| `requirements.txt` | Python dependencies |

### GitHub Details

**Repository:** https://github.com/KumudaKH/cynaris-internship-kumuda

**Branch:** `feat/w6d4-3m-kumuda`


### Day 4 Summary

Prepared an Executive Reporting System combining Vanna-based SQL analysis with a lightweight business intelligence dashboard. The project includes employee data, SQL training examples, query validation, a FastAPI endpoint and executive visualisations.

**Status:** Project files prepared; local integration testing, CIA review and GitHub submission pending.

---

## Week 6 Progress Summary

**Day 1 — W6D1:** Vanna setup, SQLite database connectivity, SQL training and FastAPI integration.

**Day 2 — W6D2:** Domain-specific Vanna training, custom SQL patterns and query validation.

**Day 3 — W6D3:** Employee Analytics Dashboard with five visualisations.

**Day 4 — W6D4:** Executive Reporting System combining Vanna SQL analysis with dashboard reporting.

**Overall Progress:** W6D1–W6D4 project implementation work prepared. Final testing, CIA review, GitHub verification and actual Apache Superset integration remain to be completed.

____________________________________________________________________________________________________________

## Day 5 — W6D5: NL SQL Dashboard on CRM Data

**Intern Name:** Kumuda KH  
**Role:** Data Analyst Intern (3 Months)  
**Date:** 20 November 2026  
**Branch:** `feat/w6d5-3m-kumuda`

### Work Completed
- Prepared a CRM Sales Intelligence Dashboard using Python, SQLite and SQL.
- Created a sample CRM database with 50 customers and 80 sales opportunities.
- Configured project components for Vanna AI and Ollama integration.
- Prepared five natural-language question–SQL training examples.
- Added ten SQL test cases for query validation.
- Developed the FastAPI endpoint `POST /cia/sql-analyst`.
- Created an HTML dashboard with bar charts, line charts, pie charts, KPI metrics and tables.
- Organised CSV datasets, SQL queries, testing files and project documentation.

### Technologies Used
Python, Vanna AI, Ollama, SQLite, SQL, FastAPI, HTML, CSS, JavaScript, VS Code, Git and GitHub.

### Challenges and Solutions
The main challenge was integrating natural-language SQL generation with CRM data while working with limited laptop storage. Used a lightweight HTML dashboard instead of Apache Superset and prepared reference SQL queries for validating results.

### Testing and Validation
- Prepared five SQL training examples and ten test cases.
- Executed reference SQL queries against the sample CRM database.
- Prepared the dashboard for browser-based viewing.
- Local Vanna/Ollama and FastAPI end-to-end testing remain pending verification.

### Learning Outcomes
- Understood natural-language-to-SQL generation using Vanna AI.
- Improved CRM database management and SQL querying skills.
- Learned how to present customer and sales insights using dashboards.
- Gained experience organising an analytics project with FastAPI and GitHub.

### Conclusion
Prepared a CRM-based natural-language SQL analytics project combining database management, AI-assisted SQL generation and business intelligence visualisations. The project demonstrates how CRM data can be analysed to support business decisions.