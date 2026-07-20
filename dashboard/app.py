# dashboard/app.py
# =====================================================
# SmartFish AI – Final Hackathon Dashboard
# Uses:
# models/fish_model.pkl
# models/scaler.pkl
# data/ocean_data_clean.csv
# =====================================================

import sys
import os
from math import radians, cos, sin, sqrt, atan2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.ocean_api import fetch_ocean_data
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.express as px
import plotly.graph_objects as go

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in KM

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="SmartFish AI",
    page_icon="🐟",
    layout="wide"
)
use_live = st.toggle("🌍 Use Live Ocean Data", value=True)
# -----------------------------------------------------
# PATHS
# -----------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "ocean_data_clean.csv")
model_path = os.path.join(BASE_DIR, "models", "fish_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

# -----------------------------------------------------
# LOAD FILES
# -----------------------------------------------------

lat = 12.97
lon = 77.59

csv_df = pd.read_csv(data_path)

if use_live:
    live_df = fetch_ocean_data(lat, lon)

    if live_df is not None:
        df = pd.concat([csv_df, live_df], ignore_index=True)
        st.success("🌊 Live Ocean Data Added")
    else:
        df = csv_df
        st.warning("⚠️ API failed, using offline data")
else:
    df = csv_df

# ✅ ADD HERE (IMPORTANT)
df = df.fillna({
    "temperature": 25,
    "salinity": 30,
    "chlorophyll": 2
})
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# -----------------------------------------------------
# UI / THEME
# -----------------------------------------------------

st.markdown("""
<style>

.main{
background: linear-gradient(135deg,#02131f,#062b3d,#0b4f6c);
color:white;
}

[data-testid="stSidebar"]{
background: linear-gradient(180deg,#a6e3ff,#d6f4ff);
padding:20px;
}

.metric-box{
background:rgba(255,255,255,0.08);
padding:18px;
border-radius:18px;
box-shadow:0 4px 20px rgba(0,0,0,0.25);
text-align:center;
}

h1,h2,h3{
color:#8eeeff;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# TITLE
# -----------------------------------------------------

st.markdown("""
<h1 style='text-align:center;'>🐟 SmartFish AI – Ocean Hotspot Predictor</h1>
<p style='text-align:center;font-size:18px;'>
AI-powered marine intelligence system for fish hotspot detection,
route guidance and sustainability insights.
</p>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# SIDEBAR INPUTS
# -----------------------------------------------------

st.sidebar.header("🌊 Ocean Conditions")

temp = st.sidebar.slider("Temperature (°C)", 10.0, 35.0, 24.0)
sal = st.sidebar.slider("Salinity (PSU)", 28.0, 40.0, 35.0)
chl = st.sidebar.slider("Chlorophyll", 0.1, 5.0, 2.0)

st.sidebar.subheader("🌊 Smart Ocean Controls")

min_prob = st.sidebar.slider("Minimum Zone Probability",0,100,50)

# -----------------------------------------------------
# PREDICTION
# -----------------------------------------------------

input_df = pd.DataFrame({
    "temperature":[temp],
    "salinity":[sal],
    "chlorophyll":[chl]
})

scaled = scaler.transform(input_df)
probability = model.predict_proba(scaled)[0][1] * 100
probability = round(probability,2)

# -----------------------------------------------------
# METRICS
# -----------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("🐟 Fish Presence", f"{probability:.2f}%")

with col2:
    if probability > 75:
        st.success("Excellent Zone")
    elif probability > 45:
        st.warning("Moderate Zone")
    else:
        st.error("Low Zone")

with col3:
    if temp > 30:
        st.error("High Temp Risk")
    else:
        st.success("Temp Stable")

with col4:
    if chl < 0.8:
        st.warning("Low Food Supply")
    else:
        st.success("Good Biomass")

# -----------------------------------------------------
# SMART FISHING ADVISOR
# -----------------------------------------------------

st.subheader("🎣 Smart Fishing Advisor")

if probability > 75:
    st.success("Deploy nets now. High fish aggregation predicted.")

elif probability > 45:
    st.warning("Moderate fish presence. Scan nearby zones.")

else:
    st.info("Move vessel to alternative zone.")

# -----------------------------------------------------
# SUSTAINABILITY
# -----------------------------------------------------

st.subheader("🌱 Sustainability Indicator")

if probability > 80:
    st.warning("Avoid overfishing. Recommended selective harvest.")
else:
    st.success("Sustainable catch conditions.")

# -----------------------------------------------------
# PREPARE MAP DATA (MOVE THIS UP ✅)
# -----------------------------------------------------

map_df = df.copy()

features = map_df[["temperature","salinity","chlorophyll"]]
scaled_map = scaler.transform(features)

map_df["predicted_probability"] = model.predict_proba(scaled_map)[:,1] * 100

filtered_df = map_df[
    map_df["predicted_probability"] >= min_prob
]

# -----------------------------------------------------
# ECONOMIC IMPACT
# -----------------------------------------------------

st.subheader("💰 Economic Impact Estimator")

expected_catch = probability * 2.5
revenue = expected_catch * 180

colA,colB = st.columns(2)

with colA:
    st.metric("Estimated Catch (kg)", f"{expected_catch:.1f}")

with colB:
    st.metric("Estimated Revenue", f"₹ {revenue:.0f}")

# -----------------------------------------------------
# REAL-TIME SCENARIO SIMULATION
# -----------------------------------------------------

st.subheader("⏱ Ocean Time Simulation")

hour = st.slider("Select Hour of Day",0,23,12)

sim_temp = temp + np.sin(hour/24 * 2*np.pi)*1.2
sim_chl = chl + np.cos(hour/24 * 2*np.pi)*0.25

st.write(f"Simulated Temperature: {sim_temp:.2f} °C")
st.write(f"Simulated Chlorophyll: {sim_chl:.2f}")

# -----------------------------------------------------
# ROUTE NAVIGATION
# -----------------------------------------------------

st.subheader("🧭 Live GPS Route Navigation")

user_lat = st.number_input("Your Latitude", value=12.9141)
user_lon = st.number_input("Your Longitude", value=74.8560)

# Copy filtered zones
route_df = filtered_df.copy()

# Calculate REAL distance in KM
route_df["distance"] = route_df.apply(
    lambda row: haversine(
        user_lat,
        user_lon,
        row["latitude"],
        row["longitude"]
    ),
    axis=1
)


# Keep only nearby zones (IMPORTANT)
route_df = route_df[route_df["distance"] <= 300]

if route_df.empty:
    st.warning("⚠️ No nearby fishing zones found.")
    st.stop()


# Score = probability - distance penalty
route_df["route_score"] = (
    route_df["predicted_probability"] - route_df["distance"] * 8
)

# Best realistic nearby zone
best = route_df.sort_values(
    by="route_score",
    ascending=False
).iloc[0]

# Route map
route = go.Figure()

route.add_trace(go.Scattermapbox(
    lat=[user_lat, best["latitude"]],
    lon=[user_lon, best["longitude"]],
    mode="lines+markers",
    line=dict(width=5, color="lime"),
    marker=dict(size=11),
    name="Best Route"
))

route.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5,
    mapbox_center={"lat": (user_lat+best["latitude"])/2,
                   "lon": (user_lon+best["longitude"])/2},
    height=550
)

st.plotly_chart(route, use_container_width=True)

st.success(
f"Recommended Zone: ({best['latitude']:.2f}, {best['longitude']:.2f})"
)

st.metric(
"Estimated Distance",
f"{best['distance']:.1f} km"
)

# -----------------------------------------------------
# GLOBAL HOTSPOT MAP
# -----------------------------------------------------

st.subheader("🌍 Global Fish Hotspot Map")

map_df = df.copy()

features = map_df[["temperature","salinity","chlorophyll"]]
scaled_map = scaler.transform(features)

map_df["predicted_probability"] = model.predict_proba(scaled_map)[:,1] * 100

filtered_df = map_df[
    map_df["predicted_probability"] >= min_prob
]

fig = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="predicted_probability",
    size="predicted_probability",
    zoom=1,
    hover_data=["temperature","salinity","chlorophyll"],
    mapbox_style="carto-positron",
    height=550
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# HEATMAP
# -----------------------------------------------------

st.subheader("🌊 Ocean Fish Density Heatmap")

heat = px.density_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    z="predicted_probability",
    radius=12,
    zoom=1,
    mapbox_style="carto-positron",
    height=550
)

st.plotly_chart(heat, use_container_width=True)

# -----------------------------------------------------
# ANIMATED HOTSPOTS
# -----------------------------------------------------

if "time_step" in filtered_df.columns:

    st.subheader("🎥 Animated Fish Hotspot Movement")

    anim = px.density_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        z="predicted_probability",
        animation_frame="time_step",
        radius=10,
        zoom=1,
        mapbox_style="carto-positron",
        height=550
    )

    st.plotly_chart(anim, use_container_width=True)

# -----------------------------------------------------
# TOP ZONES TABLE
# -----------------------------------------------------

st.subheader("🏆 Top Predicted Fishing Zones")

top = filtered_df.sort_values(
    by="predicted_probability",
    ascending=False
).head(10)

st.dataframe(
    top[[
        "latitude",
        "longitude",
        "predicted_probability"
    ]],
    use_container_width=True
)


# -----------------------------------------------------
# PIPELINE
# -----------------------------------------------------

st.subheader("🤖 SmartFish AI Pipeline")

st.write("""
1. Ocean data ingestion  
2. Cleaning & preprocessing  
3. AI probability prediction  
4. Hotspot mapping  
5. Route optimization  
6. Sustainability recommendation
""")

# -----------------------------------------------------
# AI MODEL INFO
# -----------------------------------------------------

st.subheader("🧠 AI Model Information")

st.write("Model: Random Forest Classifier")
st.write("Inputs: Temperature, Salinity, Chlorophyll")
st.write("Samples:", len(df))



# -----------------------------------------------------
# DATASET
# -----------------------------------------------------

st.subheader("📁 Ocean Dataset")

st.dataframe(df.head(), use_container_width=True)