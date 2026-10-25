import pandas as pd
from pathlib import Path

source = Path(
    r"C:\Users\KUMUDHA\Downloads\Salary_Dataset_with_Extra_Features.csv"
)

output = Path(__file__).parent / "salary_cleaned.csv"

df = pd.read_csv(source)

# Replace missing company names with a transparent placeholder
df["Company Name"] = df["Company Name"].fillna("Unknown")

df.to_csv(output, index=False)

print("Cleaned dataset created:", output)
print("Missing values remaining:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
