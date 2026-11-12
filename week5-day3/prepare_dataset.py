import pandas as pd
from pathlib import Path

source = Path("../week5-day1/Salary_Dataset_with_Extra_Features.csv")
output = Path("data/salary_100k.csv")

output.parent.mkdir(exist_ok=True)

df = pd.read_csv(source)

# Generate a reproducible 100K-row dataset
df_100k = df.sample(
    n=100000,
    replace=True,
    random_state=42
)

df_100k.to_csv(output, index=False)

print("Dataset prepared successfully!")
print("Shape:", df_100k.shape)
print("Columns:", df_100k.columns.tolist())
print("Saved to:", output)