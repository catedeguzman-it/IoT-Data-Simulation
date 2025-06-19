import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_records = 200  # Adjust as needed
origins = ["Manila", "Cebu", "Davao", "Baguio", "Bukidnon"]
destinations = ["Bulacan", "Makati", "Taguig", "Pasig", "Caloocan"]
couriers = ["LBC Express", "J&T Express", "Ninja Van", "2GO", "Flash Express"]

records = []

for _ in range(num_records):
    record = {
        "timestamp": datetime.now() - timedelta(days=np.random.randint(0, 7), minutes=np.random.randint(0, 1440)),
        "tracking_id": f"PKG{np.random.randint(1000, 9999)}",
        "device_id": f"DVC{np.random.randint(100, 999)}",
        "temperature": round(np.random.uniform(2.0, 10.0), 2),
        "humidity": round(np.random.uniform(30.0, 70.0), 2),
        "speed_kmph": round(np.random.uniform(0, 100), 2),
        "status": np.random.choice(["in_transit", "at_warehouse", "delivered", "delayed"]),
        "origin": np.random.choice(origins),
        "destination": np.random.choice(destinations),
        "weight": round(np.random.uniform(0.5, 25.0), 2),  # in kg
        "volume": round(np.random.uniform(0.01, 1.5), 2),  # in cubic meters
        "courier_name": np.random.choice(couriers)
    }
    records.append(record)

# Convert to DataFrame
df = pd.DataFrame(records)

# Save dataset
df.to_csv("smart_tracking_data.csv", index=False)
df.to_json("smart_tracking_data.json", orient="records")

# Display first few rows
df.head()
