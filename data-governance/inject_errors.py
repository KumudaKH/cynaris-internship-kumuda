import pandas as pd
from pathlib import Path

source = Path(
    r"C:\Users\KUMUDHA\Downloads\Salary_Dataset_with_Extra_Features.csv"
)

output = Path(__file__).parent / "salary_corrupted.csv"

df = pd.read_csv(source)

# Error 1: Missing job title
df.loc[df.index[0], "Job Title"] = None

# Error 2: Negative salary
df.loc[df.index[1], "Salary"] = -50000

# Error 3: Invalid rating
df.loc[df.index[2], "Rating"] = 10

df.to_csv(output, index=False)

print("Corrupted test dataset created:", output)
print("Original dataset has not been changed.")