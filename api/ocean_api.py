import requests
import pandas as pd

def fetch_ocean_data(lat, lon):
    try:
        url = f"https://marine-api.open-meteo.com/v1/marine?latitude={lat}&longitude={lon}&current=sea_surface_temperature"

        response = requests.get(url, timeout=5)
        data = response.json()

        temp = data['current']['sea_surface_temperature']

        # Convert to your model format
        df = pd.DataFrame({
            "latitude": [lat],
            "longitude": [lon],
            "temperature": [temp],
            "salinity": [30],       # placeholder (model needs it)
            "chlorophyll": [2],     # placeholder
        })

        return df

    except Exception as e:
        print("API failed:", e)
        return None