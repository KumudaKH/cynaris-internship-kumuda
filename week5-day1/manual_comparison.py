import pandas as pd
import time

# Load dataset
df = pd.read_csv("Salary_Dataset_with_Extra_Features.csv")

print("=" * 65)
print("PANDASAI VS MANUAL PANDAS COMPARISON")
print("=" * 65)

# ---------------------------------------
# QUESTION 1: Average Salary
# ---------------------------------------

print("\nQUESTION 1: What is the average salary?")

start = time.time()

manual_average = df["Salary"].mean()

manual_time = time.time() - start

print("Manual Pandas:", manual_average)

# ---------------------------------------
# QUESTION 2: Unique Companies
# ---------------------------------------

print("\nQUESTION 2: How many unique companies are present?")

start = time.time()

manual_unique = df["Company Name"].nunique()

unique_time = time.time() - start

print("Manual Pandas:", manual_unique)

# ---------------------------------------
# QUESTION 3: Top 5 Common Job Titles
# ---------------------------------------

print("\nQUESTION 3: What are the top 5 most common job titles?")

start = time.time()

manual_jobs = (
    df["Job Title"]
    .value_counts()
    .head(5)
)

job_time = time.time() - start

print("Manual Pandas:")
print(manual_jobs)

# ---------------------------------------
# SAVE COMPARISON RESULTS
# ---------------------------------------

comparison = pd.DataFrame({

    "Question": [
        "Average Salary",
        "Unique Companies",
        "Top 5 Common Job Titles"
    ],

    "Manual_Pandas_Result": [
        str(manual_average),
        str(manual_unique),
        str(manual_jobs.to_dict())
    ],

    "Manual_Execution_Time_Seconds": [
        manual_time,
        unique_time,
        job_time
    ]

})

comparison.to_csv(
    "results/manual_pandas_comparison.csv",
    index=False
)

print("\nComparison saved successfully!")

print(comparison)