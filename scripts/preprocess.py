import pandas as pd
import os

# locate project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "ocean_data.csv")
output_path = os.path.join(BASE_DIR, "data", "ocean_data_clean.csv")

print("Loading dataset...")

df = pd.read_csv(data_path)

print("Initial rows:", len(df))

# ---------------------------
# Handle missing values
# ---------------------------

df = df.dropna()

print("Rows after removing missing values:", len(df))

# ---------------------------
# Validate ocean ranges
# ---------------------------

df = df[
    (df["temperature"] >= 0) &
    (df["temperature"] <= 35) &
    (df["salinity"] >= 25) &
    (df["salinity"] <= 40) &
    (df["chlorophyll"] >= 0)
]

print("Rows after range filtering:", len(df))

# ---------------------------
# Save cleaned dataset
# ---------------------------

df.to_csv(output_path, index=False)

print("Clean dataset saved to:")
print(output_path)

print("\nPreview of cleaned data:")
print(df.head())