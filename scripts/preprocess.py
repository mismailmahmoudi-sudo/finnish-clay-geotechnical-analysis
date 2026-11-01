"""
Preprocessing of Finnish clay geotechnical laboratory data.

Laboratory 3 - ING8100
Polytechnique Montreal
"""

from pathlib import Path
import re
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Laboratory_data.xlsx"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "laboratory_data_clean.csv"


def clean_column_name(name):
    """Standardize column names."""

    name = str(name).strip().lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def preprocess_data():
    """Read, clean and export the laboratory dataset."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Raw dataset not found. Run download_data.py first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load original laboratory data
    df = pd.read_excel(INPUT_FILE)

    print("Original dimensions:", df.shape)

    # Standardize column names
    df.columns = [
        clean_column_name(column)
        for column in df.columns
    ]

    if not df.columns.is_unique:
        raise ValueError(
            "Column names are duplicated after standardization."
        )

    # Remove leading and trailing spaces in text values
    for column in df.select_dtypes(include=["object", "string"]):
        df[column] = df[column].map(
            lambda value: value.strip()
            if isinstance(value, str) else value
        )

    # Replace a common missing-value marker
    df = df.replace(r"^\s*[-–—]\s*$", pd.NA, regex=True)

    # Count missing values without removing observations
    missing_values = df.isna().sum()

    # Export processed dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print("Processed dimensions:", df.shape)
    print("Total missing values:", missing_values.sum())
    print("Processed dataset saved to:", OUTPUT_FILE)

    return df


if __name__ == "__main__":
    preprocess_data()
