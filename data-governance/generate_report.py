import json
from pathlib import Path
from datetime import datetime

folder = Path(__file__).parent

# Read actual Great Expectations results
with open(folder / "validation_results.json", encoding="utf-8") as f:
    results = json.load(f)

checks = results.get("results", [])
overall_success = results.get("success", False)

passed = sum(1 for check in checks if check.get("success"))
failed = len(checks) - passed

rows = ""

for check in checks:
    config = check.get("expectation_config", {})
    name = config.get("type", "Unknown expectation")
    kwargs = config.get("kwargs", {})
    column = kwargs.get("column", "Whole dataset")
    status = "PASS" if check.get("success") else "FAIL"

    result_data = check.get("result", {})
    unexpected = result_data.get("unexpected_count", 0)

    rows += f"""
    <tr>
      <td>{name}</td>
      <td>{column}</td>
      <td class="{status.lower()}">{status}</td>
      <td>{unexpected}</td>
    </tr>
    """

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Salary Dataset Data Quality Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 35px;
    background: #f5f7fa;
    color: #222;
}}
h1, h2 {{ color: #243b53; }}
.card {{
    background: white;
    padding: 20px;
    margin: 15px 0;
    border-radius: 8px;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
}}
th, td {{
    padding: 12px;
    border: 1px solid #ddd;
    text-align: left;
}}
th {{ background: #243b53; color: white; }}
.pass {{ color: green; font-weight: bold; }}
.fail {{ color: #c62828; font-weight: bold; }}
</style>
</head>
<body>
<h1>Data Quality Validation Report</h1>

<div class="card">
<p><strong>Dataset:</strong> Software Professional Salaries 2022</p>
<p><strong>Rows:</strong> 22,770</p>
<p><strong>Columns:</strong> 8</p>
<p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
<p><strong>Overall validation:</strong>
<span class="{'pass' if overall_success else 'fail'}">
{"PASSED" if overall_success else "FAILED"}
</span></p>
<p><strong>Checks passed:</strong> {passed}</p>
<p><strong>Checks failed:</strong> {failed}</p>
</div>

<h2>Expectation Results</h2>
<table>
<tr>
<th>Expectation</th>
<th>Column</th>
<th>Status</th>
<th>Unexpected Count</th>
</tr>
{rows}
</table>

<div class="card">
<h2>Recommendations</h2>
<ul>
<li>Investigate and resolve missing company names.</li>
<li>Keep salary values positive and ratings within the permitted range.</li>
<li>Run validation before refreshing downstream dashboards.</li>
<li>Review dataset freshness and source reliability.</li>
</ul>
</div>
</body>
</html>
"""

report_path = folder / "great_expectations_report.html"
report_path.write_text(html, encoding="utf-8")

print("HTML report created:", report_path)
print(f"Passed: {passed}; Failed: {failed}")