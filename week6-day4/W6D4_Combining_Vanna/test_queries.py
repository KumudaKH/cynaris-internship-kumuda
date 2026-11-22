"""10 reference SQL tests; optional --vanna to compare AI-generated results."""
import argparse, csv, json
from pathlib import Path
from sql_patterns import TESTS
from query_engine import execute_readonly
parser=argparse.ArgumentParser()
parser.add_argument('--vanna', action='store_true', help='Test generated SQL with local Vanna/Ollama')
args=parser.parse_args()
vn=None
if args.vanna:
    from vanna_setup import get_vanna
    vn=get_vanna()
results=[]
for n,(question,reference_sql) in enumerate(TESTS,1):
    generated=''
    try:
        expected=execute_readonly(reference_sql)
        if vn:
            generated=vn.generate_sql(question=question,allow_llm_to_see_data=False)
            actual=execute_readonly(generated)
            # Row ordering ignored; review ORDER BY and LIMIT manually.
            status='PASS' if sorted(map(str,actual))==sorted(map(str,expected)) else 'FAIL'
        else:
            status='REFERENCE_PASS'
        error=''
    except Exception as exc:
        status='ERROR'; error=str(exc)
    print(f'{n:02} {status}: {question}')
    results.append({'number':n,'question':question,'reference_sql':reference_sql,'generated_sql':generated,'status':status,'error':error})
with (Path(__file__).resolve().parent/'test_results.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=results[0].keys());writer.writeheader();writer.writerows(results)
print('Saved test_results.csv. REFERENCE_PASS does not mean Vanna was tested.')
