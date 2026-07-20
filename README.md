SmartFish AI – Ocean Hotspot Predictor

An AI-powered web application that predicts potential fish hotspot locations using ocean environmental parameters. The project helps fishermen and marine researchers identify high-probability fishing zones through machine learning, interactive maps, and data visualization.

📌 Project Overview

SmartFish AI uses ocean parameters such as temperature, salinity, and chlorophyll concentration to predict the probability of fish presence. The system provides intelligent fishing recommendations and visualizes fish hotspots on an interactive world map.

The project demonstrates how Artificial Intelligence, Machine Learning, and Data Visualization can support sustainable fishing and marine resource management.

🚀 Features
Ocean Conditions Panel
Temperature input
Salinity input
Chlorophyll concentration input
AI Fish Presence Prediction
Predicts fish presence probability using a trained Random Forest Machine Learning model
Smart Fishing Recommendation
Low Fishing Potential
Moderate Fishing Potential
High Fishing Potential
Interactive Global Fish Hotspot Map
Ocean Fish Density Heatmap
Top Predicted Fishing Zones
Environmental Insights Dashboard
Animated Fish Hotspot Movement
Ocean Dataset Viewer
AI Model Information
Sustainability Indicator
Ocean Risk Alerts
Economic Impact Estimator
Live GPS Tracking (Prototype)
Ocean Scenario Simulation
🛠️ Technology Stack

Programming Language

Python

Framework

Streamlit

Machine Learning

Scikit-learn
Random Forest Classifier

Data Processing

Pandas
NumPy

Visualization

Plotly
Mapbox

Model Storage

Joblib
📂 Project Structure

Smartfish_AI/

├── dashboard/
│ └── app.py

├── data/
│ ├── ocean_data.csv
│ └── ocean_data_clean.csv

├── models/
│ ├── fish_model.pkl
│ └── scaler.pkl

├── scripts/
│ ├── generate_data.py
│ ├── preprocess.py
│ ├── train_model.py
│ └── save_model.py

├── requirements.txt

├── README.md

└── LICENSE


▶️ Running the Application

Run the Streamlit application using:

streamlit run dashboard/app.py

The dashboard will automatically open in your default web browser.

🧠 Machine Learning Workflow

Ocean Dataset

↓

Data Preprocessing

↓

Feature Scaling

↓

Random Forest Model Training

↓

Model Saving (Joblib)

↓

Prediction

↓

Interactive Streamlit Dashboard

## Installation

1. Clone the repository

```bash
git clone https://github.com/Spurthi1237/Smart_Fish-AI-Project.git
```

2. Navigate to the project folder

```bash
cd Smart_Fish-AI-Project
```

3. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies

```bash
pip install -r requirements.txt
```

## How to Run

1. Open a terminal inside the project directory.

2. Start the Streamlit application.

```bash
streamlit run dashboard/app.py
```

3. Open your browser and visit

```
http://localhost:8501
```

4. Adjust the ocean parameters using the dashboard controls and click **Predict** to view:
- Fish hotspot probability
- Fishing recommendation
- Interactive hotspot map
- Heatmap
- Environmental insights

📊 Input Parameters
Water Temperature (°C)
Salinity (PSU)
Chlorophyll Concentration (mg/m³)
📤 Output
Fish Presence Probability
Smart Fishing Recommendation
Interactive Fish Hotspot Map
Ocean Density Heatmap
Environmental Insights
Predicted Fishing Zones
🌍 Applications
Smart Fishing
Marine Research
Fisheries Management
Sustainable Fishing
Ocean Data Analysis
Educational Demonstrations
🔮 Future Enhancements
Real-time Ocean API Integration
Satellite Data Support
Weather Forecast Integration
Mobile Application
Multi-species Fish Prediction
Deep Learning Models
Route Optimization for Fishing Boats
Historical Ocean Trend Analysis

📈 Project Workflow

User Inputs Ocean Parameters

↓

AI Predicts Fish Presence Probability

↓

Fishing Recommendation Generated

↓

Interactive Maps & Visualizations Displayed

↓

Decision Support for Fishermen and Researchers

👨‍💻 Author

Spurthi A

Engineering Student | AI & Machine Learning Enthusiast

📜 License

This project is licensed under the MIT License.

⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. Your support is appreciated!
