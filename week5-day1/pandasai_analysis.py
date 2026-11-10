import logging
from pathlib import Path

import pandas as pd
import pandasai as pai

from pandasai_litellm.litellm import LiteLLM


# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "Salary_Dataset_with_Extra_Features.csv"

LOG_DIR = BASE_DIR / "logs"
RESULT_DIR = BASE_DIR / "results"

LOG_DIR.mkdir(exist_ok=True)
RESULT_DIR.mkdir(exist_ok=True)


# =====================================================
# 2. LOGGING CONFIGURATION
# =====================================================

logging.basicConfig(
    filename=str(LOG_DIR / "pandasai_errors.log"),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


# =====================================================
# 3. OLLAMA CONFIGURATION
# =====================================================

llm = LiteLLM(
    model="ollama/qwen3:8b",
    api_base="http://localhost:11434"
)

pai.config.set({
    "llm": llm,
    "verbose": True,
    "max_retries": 2
})

print("\nPandasAI configured with Ollama Qwen3 8B")


# =====================================================
# 4. LOAD DATASET
# =====================================================

try:

    raw_df = pd.read_csv(DATASET_PATH)

    # Standardize column names
    raw_df.columns = (
        raw_df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    # Validate required columns
    required_columns = [
        "rating",
        "company_name",
        "job_title",
        "salary",
        "salaries_reported",
        "location",
        "employment_status",
        "job_roles"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in raw_df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing dataset columns: {missing_columns}"
        )

    # Convert numeric columns
    for column in [
        "rating",
        "salary",
        "salaries_reported"
    ]:

        raw_df[column] = pd.to_numeric(
            raw_df[column],
            errors="coerce"
        )

    # Create PandasAI DataFrame
    df = pai.DataFrame(raw_df)

    print("\nDataset Loaded Successfully!")
    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

except Exception:

    logging.exception("Dataset loading failed")
    raise


# =====================================================
# 5. NATURAL LANGUAGE QUERIES
# =====================================================

queries = [

    "Count the total number of records.",

    "Calculate the average rating.",

    "Find the top 10 companies by average salary. "
    "Return company_name and average_salary.",

    "Calculate the average salary.",

    "Find the location with the highest average salary.",

    "Count the number of unique companies.",

    "Find the top 5 most frequently occurring job titles.",

    "Calculate average salary grouped by employment_status.",

    "Find the job_role with the highest average salary.",

    "Find the top 10 highest-paying job_titles "
    "based on average salary."

]


# =====================================================
# 6. EXECUTE NATURAL LANGUAGE QUERIES
# =====================================================

results = []

for index, query in enumerate(queries, start=1):

    print("\n" + "=" * 65)
    print(f"QUERY {index}: {query}")
    print("=" * 65)

    try:

        response = df.chat(query)

        print("\nRESULT:")
        print(response)

        response_text = str(response)

        # Detect PandasAI error responses
        if (
            "Unfortunately, I was not able to get your answer"
            in response_text
        ):

            status = "FAILED"

            logging.error(
                "PandasAI ErrorResponse - Query %s: %s",
                index,
                query
            )

        else:

            status = "SUCCESS"

        results.append({
            "query_number": index,
            "question": query,
            "result": response_text,
            "status": status
        })

    except Exception as error:

        print("\nQUERY FAILED:")
        print(error)

        logging.exception(
            "Query %s failed: %s",
            index,
            query
        )

        results.append({
            "query_number": index,
            "question": query,
            "result": str(error),
            "status": "FAILED"
        })


# =====================================================
# 7. SAVE RESULTS
# =====================================================

results_df = pd.DataFrame(results)

output_path = RESULT_DIR / "pandasai_query_results.csv"

results_df.to_csv(
    output_path,
    index=False
)


# =====================================================
# 8. EXECUTION SUMMARY
# =====================================================

success_count = (
    results_df["status"] == "SUCCESS"
).sum()

failed_count = (
    results_df["status"] == "FAILED"
).sum()

print("\n" + "=" * 65)
print("PANDASAI ANALYSIS COMPLETED")
print("=" * 65)

print("\nTotal Queries:", len(queries))
print("Successful Queries:", success_count)
print("Failed Queries:", failed_count)

print("\nExecution Details:")

print(
    results_df[
        ["query_number", "status"]
    ].to_string(index=False)
)

print("\nResults saved to:")
print(output_path)

print("\nError logs saved to:")
print(LOG_DIR / "pandasai_errors.log")