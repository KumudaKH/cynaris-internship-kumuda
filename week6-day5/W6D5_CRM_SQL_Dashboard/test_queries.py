import csv
from pathlib import Path
from vanna_setup import get_vanna
from query_engine import run_select
from sql_patterns import TRAINING_PAIRS

BASE = Path(__file__).resolve().parent
TESTS = TRAINING_PAIRS + [
    ('How many opportunities are there?', 'SELECT COUNT(*) AS total_opportunities FROM opportunities'),
    ('How many deals are won?', "SELECT COUNT(*) AS won_deals FROM opportunities WHERE stage='Won'"),
    ('Count customers by region', 'SELECT region, COUNT(*) AS customer_count FROM customers GROUP BY region ORDER BY region'),
    ('List the five largest opportunities', 'SELECT opportunity_id, amount FROM opportunities ORDER BY amount DESC, opportunity_id LIMIT 5'),
    ('Show won revenue by industry', "SELECT c.industry, SUM(o.amount) AS revenue FROM opportunities o JOIN customers c ON c.customer_id=o.customer_id WHERE o.stage='Won' GROUP BY c.industry ORDER BY c.industry")
]

def comparable(rows):
    return sorted([tuple(sorted(row.values(), key=str)) for row in rows], key=str)

def main():
    vn = get_vanna()
    results = []
    for i, (question, expected_sql) in enumerate(TESTS, 1):
        generated_sql = ''
        try:
            generated_sql = vn.generate_sql(question=question, allow_llm_to_see_data=False)
            actual = run_select(generated_sql)
            expected = run_select(expected_sql)
            status = 'PASS' if comparable(actual) == comparable(expected) else 'FAIL'
        except Exception as exc:
            status = 'ERROR: ' + str(exc)
        print(i, status, question)
        results.append({'number': i, 'question': question, 'generated_sql': generated_sql, 'reference_sql': expected_sql, 'status': status})
    with (BASE/'test_results.csv').open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys()); writer.writeheader(); writer.writerows(results)
    print('Passed', sum(r['status']=='PASS' for r in results), 'of', len(results))

if __name__ == '__main__':
    main()
