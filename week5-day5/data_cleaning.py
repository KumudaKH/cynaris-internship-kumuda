import pandas as pd
import os

# Define dataset paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "startup_funding.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned_indian_business_dataset.csv")


def load_dataset():
    """Load the Indian business dataset."""
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    print("\nDataset loaded successfully!")
    print("Original Shape:", df.shape)
    return df


def clean_dataset(df):
    """Clean and preprocess the dataset."""

    # Remove duplicate records
    df = df.drop_duplicates()

    # Replace common missing value representations
    df.replace(["", " ", "NA", "N/A", "null", "NULL", "Unknown"], pd.NA, inplace=True)

    # Display missing values
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Handle missing values
    for column in df.columns:
        if df[column].isnull().any():

            if df[column].dtype == "object":
                df[column] = df[column].fillna("Not Available")
            else:
                df[column] = df[column].fillna(df[column].median())

    # Clean column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )

    print("\nCleaning completed!")
    print("Cleaned Shape:", df.shape)

    return df

    # Convert funding amount to numeric
    if "amount_in_usd" in df.columns:
      df["amount_in_usd"] = (
        df["amount_in_usd"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

    df["amount_in_usd"] = pd.to_numeric(
        df["amount_in_usd"],
        errors="coerce"
    )

    print("\nFunding Amount Data Type:")
    print(df["amount_in_usd"].dtype)

def save_dataset(df):
    """Save the cleaned dataset."""
    # Convert funding amount to numeric
    df["amount_in_usd"] = (
    df["amount_in_usd"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

    df["amount_in_usd"] = pd.to_numeric(
    df["amount_in_usd"],
    errors="coerce"
)

    print("\nFunding Amount Data Type:")
    print(df["amount_in_usd"].dtype)
    df.to_csv(OUTPUT_PATH, index=False)
    print("\nCleaned dataset saved at:", OUTPUT_PATH)


if __name__ == "__main__":
    dataset = load_dataset()
    cleaned_dataset = clean_dataset(dataset)
    save_dataset(cleaned_dataset)

    print("\nFinal Dataset Preview:")
    print(cleaned_dataset.head())