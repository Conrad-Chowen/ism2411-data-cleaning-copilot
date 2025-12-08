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

# Remove extra whitespace from string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Handle missing values
if 'quantity' in df.columns:
    df['quantity'] = df['quantity'].fillna(0)  # fill missing quantities with 0
if 'price' in df.columns:
    df['price'] = df['price'].fillna(df['price'].median())  # fill missing prices with median

# Remove invalid rows with negative quantity or price
df = df[(df['quantity'] >= 0) & (df['price'] >= 0)]

# Create processed folder if it doesn't exist and save cleaned CSV
os.makedirs(os.path.join(BASE_DIR, "data/processed"), exist_ok=True)
df.to_csv(CLEAN_PATH, index=False)

# Print first few rows to verify
print("Cleaning complete. First few rows:")
print(df.head())
