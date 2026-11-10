import pandas as pd
import pandasai as pai

from pandasai_litellm.litellm import LiteLLM

# Configure Ollama
llm = LiteLLM(
    model="ollama/llama3.2:latest",
    api_base="http://localhost:11434"
)

pai.config.set({
    "llm": llm,
    "verbose": True,
    "max_retries": 3
})

# Create sample DataFrame
df = pai.DataFrame({
    "Employee": ["A", "B", "C", "D"],
    "Salary": [30000, 40000, 50000, 60000]
})

# Ask PandasAI
response = df.chat(
    "What is the average salary? "
    "Use execute_sql_query() for SQL execution. "
    "Do not import duckdb or create database connections. "
    "Use AVG(Salary) AS average_salary in SQL. "
    "Access the result using result_df['average_salary'].iloc[0]. "
    "Return the result as a number."
)

print("\nFinal Answer:")
print(response)