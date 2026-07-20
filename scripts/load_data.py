import pandas as pd

# Load dataset from data folder
data = pd.read_csv("../data/ocean_data.csv")

# Show first 5 rows
print(data.head())