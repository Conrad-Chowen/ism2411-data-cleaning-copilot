# Purpose: Clean the raw sales dataset by standardizing column names,
# stripping whitespace, handling missing values, and removing invalid rows.

import pandas as pd

# Copilot-assisted function #1
# This function loads a CSV file into a DataFrame.
def load_data(file_path: str):
    """
    Load CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)

# Copilot-assisted function #2
# Standardizes column names to lowercase and underscores.
def clean_column_names(df):
    """
    Standardize column names: lowercase and replace spaces with underscores.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def strip_whitespace(df):
    """
    Remove leading/trailing whitespace from string columns like product names and categories.
    """
    str_cols = df.select_dtypes(include='object').columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    return df

def handle_missing_values(df):
    """
    Drop rows with missing price or quantity.
    """
    df = df.dropna(subset=['price', 'quantity'])
    return df

def remove_invalid_rows(df):
    """
    Remove rows where price or quantity is negative.
    """
    df = df[df['price'] >= 0]
    df = df[df['quantity'] >= 0]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load raw data
    df_raw = load_data(raw_path)

    # Clean column names
    df_clean = clean_column_names(df_raw)

    # Strip whitespace from text columns
    df_clean = strip_whitespace(df_clean)

    # Handle missing values
    df_clean = handle_missing_values(df_clean)

    # Remove invalid rows
    df_clean = remove_invalid_rows(df_clean)

    # Save cleaned CSV
    df_clean.to_csv(cleaned_path, index=False)

    # Preview first few rows
    print("Cleaning complete. First few rows:")
    print(df_clean.head())

