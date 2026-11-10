import pandas as pd

df = pd.read_csv("Salary_Dataset_with_Extra_Features.csv")

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

print("=" * 65)
print("SALARY OUTLIER VALIDATION")
print("=" * 65)

# 1. Salary statistics
print("\n1. SALARY STATISTICS")
print(df["Salary"].describe())

# 2. Highest individual salaries
print("\n2. TOP 10 HIGHEST INDIVIDUAL SALARIES")
print(
    df[["Company Name", "Job Title", "Salary"]]
    .sort_values("Salary", ascending=False)
    .head(10)
    .to_string(index=False)
)

# 3. Companies with highest average salaries
print("\n3. TOP 10 COMPANIES BY AVERAGE SALARY")

company_salary = (
    df.groupby("Company Name")["Salary"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(company_salary)

# 4. Check unusually high salaries
print("\n4. SALARIES ABOVE 10 LAKH")
print("Count:", (df["Salary"] > 1000000).sum())

print("\n5. SALARIES ABOVE 50 LAKH")
print("Count:", (df["Salary"] > 5000000).sum())

print("\nValidation completed.")