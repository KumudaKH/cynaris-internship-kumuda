import pandas as pd
import numpy as np

np.random.seed(42)

n = 100000

data = {
    "employee_id": range(1, n + 1),
    "department": np.random.choice(
        ["IT", "HR", "Finance", "Sales", "Marketing"], n
    ),
    "salary": np.random.randint(20000, 150000, n),
    "experience": np.random.randint(0, 20, n),
    "age": np.random.randint(21, 60, n),
    "performance_rating": np.random.randint(1, 6, n)
}

df = pd.DataFrame(data)

df.to_csv("employee_data_100k.csv", index=False)

print("Dataset created successfully!")
print("Shape:", df.shape)
print(df.head())