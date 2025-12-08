"""
data_cleaning.py

Purpose: Load a messy sales dataset, clean it (standardize column names, handle missing values, remove invalid rows),
and save the cleaned data for analysis.
"""

import pandas as pd
import os

# Set base directory relative to this script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define file paths
RAW_PATH = os.path.join(BASE_DIR, "data/raw/sales_data_raw.csv")
CLEAN_PATH = os.path.join(BASE_DIR, "data/processed/sales_data_clean.csv")

# Load the raw CSV data
df = pd.read_csv(RAW_PATH)

# Standardize column names: lowercase and replace spaces with underscores
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
print("Columns after cleaning:", df.columns.tolist())

# Remove extra whitespace from string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Convert columns to numeric; invalid entries become NaN
if 'price' in df.columns:
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
if 'qty' in df.columns:  # updated column name
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

# Fill missing values with median (only if the column exists)
if 'price' in df.columns:
    df['price'] = df['price'].fillna(df['price'].median())
if 'qty' in df.columns:  # updated column name
    df['qty'] = df['qty'].fillna(df['qty'].median())

# Remove rows with negative price or quantity if columns exist
if 'price' in df.columns:
    df = df[df['price'] >= 0]
if 'qty' in df.columns:  # updated column name
    df = df[df['qty'] >= 0]

# Create processed folder if it doesn't exist and save cleaned CSV
os.makedirs(os.path.join(BASE_DIR, "data/processed"), exist_ok=True)
df.to_csv(CLEAN_PATH, index=False)

# Print first few rows to verify
print("Cleaning complete. First few rows:")
print(df.head())
