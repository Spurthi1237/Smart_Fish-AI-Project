import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "ocean_data_clean.csv")
model_dir = os.path.join(BASE_DIR, "models")

os.makedirs(model_dir, exist_ok=True)

# Load data
data = pd.read_csv(data_path)

# Create smooth fish score
temp_score = np.exp(-((data["temperature"] - 24) / 5) ** 2)
sal_score = np.exp(-((data["salinity"] - 35) / 2) ** 2)
chl_score = data["chlorophyll"] / data["chlorophyll"].max()

data["fish_score"] = 0.4*temp_score + 0.3*sal_score + 0.3*chl_score
data["fish_score"] = data["fish_score"] / data["fish_score"].max()

data["fish_presence"] = (data["fish_score"] > 0.45).astype(int)

# Features
X = data[["temperature","salinity","chlorophyll"]]
y = data["fish_presence"]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model
model = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42)
model.fit(X_scaled, y)

# Save
joblib.dump(model, os.path.join(model_dir, "fish_model.pkl"))
joblib.dump(scaler, os.path.join(model_dir, "scaler.pkl"))

print("✅ Model trained successfully!")