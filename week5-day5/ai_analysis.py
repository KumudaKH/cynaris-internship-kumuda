import os
import re
import pandas as pd
import duckdb
import requests

# --------------------------------------------------
# File Paths and Configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "cleaned_indian_business_dataset.csv"
)

REPORT_PATH = os.path.join(
    BASE_DIR,
    "reports",
    "ai_business_insights.md"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:latest"


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

def load_dataset():

    df = pd.read_csv(DATA_PATH)

    print(f"Dataset loaded successfully: {df.shape}")

    return df


# --------------------------------------------------
# 2. SQL-Based Business Analysis
# --------------------------------------------------

def perform_sql_analysis(df):

    con = duckdb.connect()

    con.register("startups", df)

    results = {}

    print("\nStarting SQL-based business analysis...")

    # Total number of unique startups
    results["total_startups"] = con.execute("""
        SELECT COUNT(DISTINCT startup_name)
        FROM startups
        WHERE startup_name IS NOT NULL
        AND startup_name != 'Not Available'
    """).fetchone()[0]

    # Top startup cities
    results["top_city"] = con.execute("""
        SELECT
            city__location,
            COUNT(*) AS startup_count
        FROM startups
        WHERE city__location IS NOT NULL
        AND city__location != 'Not Available'
        GROUP BY city__location
        ORDER BY startup_count DESC
        LIMIT 5
    """).df()

    # Industries receiving the highest funding
    results["top_industries"] = con.execute("""
        SELECT
            industry_vertical,
            ROUND(SUM(amount_in_usd), 2) AS total_funding
        FROM startups
        WHERE amount_in_usd IS NOT NULL
        AND industry_vertical != 'Not Available'
        GROUP BY industry_vertical
        ORDER BY total_funding DESC
        LIMIT 10
    """).df()

    # Top 10 startups by funding
    results["top_startups"] = con.execute("""
        SELECT
            startup_name,
            ROUND(SUM(amount_in_usd), 2) AS total_funding
        FROM startups
        WHERE amount_in_usd IS NOT NULL
        AND startup_name != 'Not Available'
        GROUP BY startup_name
        ORDER BY total_funding DESC
        LIMIT 10
    """).df()

    # Most common investment types
    results["investment_types"] = con.execute("""
        SELECT
            investmentntype,
            COUNT(*) AS total_count
        FROM startups
        WHERE investmentntype IS NOT NULL
        AND investmentntype != 'Not Available'
        GROUP BY investmentntype
        ORDER BY total_count DESC
        LIMIT 10
    """).df()

    # Yearly startup funding trends
    results["yearly_trends"] = con.execute("""
        SELECT
            YEAR(
                TRY_STRPTIME(date_ddmmyyyy, '%d/%m/%Y')
            ) AS funding_year,
            COUNT(*) AS number_of_deals,
            ROUND(SUM(amount_in_usd), 2) AS total_funding
        FROM startups
        WHERE TRY_STRPTIME(
            date_ddmmyyyy,
            '%d/%m/%Y'
        ) IS NOT NULL
        GROUP BY funding_year
        ORDER BY funding_year
    """).df()

    con.close()

    print("SQL analysis completed successfully!")

    return results


# --------------------------------------------------
# 3. Generate AI Business Insights Using Ollama
# --------------------------------------------------

def generate_ai_insights(results):

    prompt = f"""
You are an Indian startup funding data analyst.

Analyze the following dataset statistics.

Total startups: {results['total_startups']}

Top cities:
{results['top_city'].to_string(index=False)}

Top industries:
{results['top_industries'].to_string(index=False)}

Top funded startups:
{results['top_startups'].to_string(index=False)}

Investment types:
{results['investment_types'].to_string(index=False)}

Yearly trends:
{results['yearly_trends'].to_string(index=False)}

Provide:

1. Three important business insights.
2. Two major startup funding trends.
3. Two practical recommendations.

Use concise and professional language.
Use only the supplied statistics.
Do not invent numbers or facts.
"""

    print("\nGenerating AI business insights using Ollama...")
    print(f"Model: {MODEL_NAME}")

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_predict": 350
                }
            },
            timeout=(10, 180)
        )

        response.raise_for_status()

        answer = response.json().get("response", "")

        answer = re.sub(
            r"<think>.*?</think>",
            "",
            answer,
            flags=re.DOTALL
        ).strip()

        if not answer:
            raise ValueError("Ollama returned an empty response.")

        print("AI insights generated successfully!")

        return answer

    except requests.exceptions.Timeout:

        print("AI generation timed out.")

        return (
            "AI insights could not be generated because "
            "the local Ollama model exceeded the time limit. "
            "Please retry with a smaller model."
        )

    except requests.exceptions.RequestException as error:

        print(f"Ollama connection error: {error}")

        return (
            "AI insights could not be generated because "
            "Ollama was unavailable. Please check whether "
            "the Ollama service is running."
        )


# --------------------------------------------------
# 4. Save Analysis Report
# --------------------------------------------------

def save_report(results, ai_insights):

    os.makedirs(
        os.path.dirname(REPORT_PATH),
        exist_ok=True
    )

    with open(
        REPORT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "# AI-Powered EDA: Indian Startup Funding Dataset\n\n"
        )

        file.write("## 1. Total Startups\n\n")

        file.write(
            f"Total unique startups: **{results['total_startups']}**\n\n"
        )

        file.write("## 2. Top Startup Cities\n\n")

        file.write(
            results["top_city"].to_markdown(index=False)
        )

        file.write("\n\n")

        file.write("## 3. Top Funded Industries\n\n")

        file.write(
            results["top_industries"].to_markdown(index=False)
        )

        file.write("\n\n")

        file.write("## 4. Top 10 Funded Startups\n\n")

        file.write(
            results["top_startups"].to_markdown(index=False)
        )

        file.write("\n\n")

        file.write("## 5. Common Investment Types\n\n")

        file.write(
            results["investment_types"].to_markdown(index=False)
        )

        file.write("\n\n")

        file.write("## 6. Yearly Funding Trends\n\n")

        file.write(
            results["yearly_trends"].to_markdown(index=False)
        )

        file.write("\n\n")

        file.write("## 7. AI-Generated Business Insights\n\n")

        file.write(ai_insights)

        file.write("\n")

    print(f"\nReport saved successfully: {REPORT_PATH}")


# --------------------------------------------------
# 5. Main Execution
# --------------------------------------------------

def main():

    print("=" * 55)
    print("AI-POWERED EDA ON INDIAN STARTUP FUNDING DATA")
    print("=" * 55)

    # Load dataset
    df = load_dataset()

    # Perform SQL analysis
    results = perform_sql_analysis(df)

    # Generate AI insights
    ai_insights = generate_ai_insights(results)

    # Save final report
    save_report(results, ai_insights)

    print("\n" + "=" * 55)
    print("AI-POWERED EDA COMPLETED SUCCESSFULLY!")
    print("=" * 55)


if __name__ == "__main__":
    main()