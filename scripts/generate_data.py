import pandas as pd
import numpy as np
import os

np.random.seed(42)

rows = 5000
time_steps = 20

data = []

for t in range(time_steps):

    hotspot_lat = np.sin(t/3)*30
    hotspot_lon = np.cos(t/3)*60

    for i in range(rows//time_steps):

        lat = np.random.uniform(-60,60)
        lon = np.random.uniform(-180,180)

        temperature = np.random.uniform(5,30)
        salinity = np.random.uniform(30,37)
        chlorophyll = np.random.uniform(0.1,3)

        dist = np.sqrt((lat-hotspot_lat)**2 + (lon-hotspot_lon)**2)

        # environmental preference
        temp_factor = np.exp(-((temperature-22)**2)/20)
        sal_factor = np.exp(-((salinity-34.5)**2)/2)
        chl_factor = np.tanh(chlorophyll)

        hotspot_factor = np.exp(-dist/25)

        fish_prob = temp_factor * sal_factor * chl_factor * hotspot_factor

        data.append([
            lat,
            lon,
            temperature,
            salinity,
            chlorophyll,
            fish_prob,
            t
        ])

df = pd.DataFrame(data,columns=[
"latitude",
"longitude",
"temperature",
"salinity",
"chlorophyll",
"fish_probability",
"time_step"
])

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output_path = os.path.join(base_dir,"data","ocean_data.csv")

df.to_csv(output_path,index=False)

print("Dataset generated successfully")
print("Total rows:",len(df))