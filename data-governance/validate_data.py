import json
from pathlib import Path

import pandas as pd
import great_expectations as gx

CSV_PATH = Path(__file__).parent / "salary_cleaned.csv"

OUTPUT_DIR = Path(__file__).parent
df = pd.read_csv(CSV_PATH)

context = gx.get_context()

# Create an expectation suite
suite = context.suites.add(
    gx.ExpectationSuite(name="salary_data_quality_suite")
)

# Define eight expectations
expectations = [
    gx.expectations.ExpectTableRowCountToBeBetween(min_value=1),

    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="Company Name"
    ),

    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="Job Title"
    ),

    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="Salary"
    ),

    gx.expectations.ExpectColumnValuesToBeBetween(
        column="Salary",
        min_value=1
    ),

    gx.expectations.ExpectColumnValuesToBeBetween(
        column="Rating",
        min_value=0,
        max_value=5
    ),

    gx.expectations.ExpectColumnValuesToBeBetween(
        column="Salaries Reported",
        min_value=1
    ),

    gx.expectations.ExpectColumnValuesToBeInSet(
        column="Employment Status",
        value_set=df["Employment Status"].dropna().unique().tolist()
    ),
]

for expectation in expectations:
    suite.add_expectation(expectation)

# Create a DataFrame asset
data_source = context.data_sources.add_pandas(
    name="salary_pandas_source"
)

data_asset = data_source.add_dataframe_asset(
    name="salary_dataframe"
)

batch_definition = data_asset.add_batch_definition_whole_dataframe(
    name="salary_batch"
)

batch = batch_definition.get_batch(
    batch_parameters={"dataframe": df}
)

# Run validation
results = batch.validate(suite)
result_dict = results.to_json_dict()

# Save validation results
with open(
    OUTPUT_DIR / "validation_results.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(result_dict, f, indent=2)

print("Great Expectations validation completed.")
print("Overall success:", result_dict.get("success"))

for result in result_dict.get("results", []):
    name = result.get("expectation_config", {}).get("type", "unknown")
    status = "PASS" if result.get("success") else "FAIL"
    print(f"{name}: {status}")

print("Saved: validation_results.json")
