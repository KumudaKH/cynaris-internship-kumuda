import os
import pandas as pd
import sweetviz as sv
from autoviz import AutoViz_Class

# Define project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR, "data", "cleaned_indian_business_dataset.csv"
)

REPORT_DIR = os.path.join(BASE_DIR, "reports")
VISUAL_DIR = os.path.join(BASE_DIR, "evidence", "autoviz")

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(VISUAL_DIR, exist_ok=True)


def load_data():
    """Load cleaned Indian business dataset."""
    df = pd.read_csv(DATA_PATH)
    print("Cleaned dataset loaded:", df.shape)
    return df


def generate_sweetviz_report(df):
    """Generate automated EDA report using SweetViz."""

    print("\nGenerating SweetViz report...")

    report = sv.analyze(df)

    report_path = os.path.join(
        REPORT_DIR, "sweetviz_eda_report.html"
    )

    report.show_html(report_path, open_browser=False)

    print("SweetViz report saved:", report_path)


def generate_autoviz_report(df):
    """Generate automated visualizations using AutoViz."""

    print("\nGenerating AutoViz visualizations...")

    AV = AutoViz_Class()

    AV.AutoViz(
        filename="",
        dfte=df,
        chart_format="png",
        verbose=1,
        max_rows_analyzed=150000,
        max_cols_analyzed=30,
        save_plot_dir=VISUAL_DIR
    )

    print("AutoViz visualizations saved:", VISUAL_DIR)


def main():
    df = load_data()

    generate_sweetviz_report(df)

    generate_autoviz_report(df)

    print("\nAutomated EDA completed successfully!")


if __name__ == "__main__":
    main()