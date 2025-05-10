import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_records = 100  # Adjust this as needed

# Example for Smart Logistics Tracking
data = []

for _ in range(num_records):
    record = {
        "timestamp": datetime.now() - timedelta(minutes=np.random.randint(0, 1440)),  # Last 24 hours
        "tracking_id": f"PKG{np.random.randint(1000, 9999)}",  # Package tracking ID
        "device_id": f"DVC{np.random.randint(100, 999)}",  # IoT device ID
        "latitude": round(np.random.uniform(40.7128, 40.7300), 6),  # Random lat in NYC range
        "longitude": round(np.random.uniform(-74.0060, -73.9352), 6),  # Random long in NYC range
        "temperature": round(np.random.uniform(2.0, 10.0), 2),  # °C for cold chain logistics
        "humidity": round(np.random.uniform(30.0, 70.0), 2),  # %
        "speed_kmph": round(np.random.uniform(0, 100), 2),
        "status": np.random.choice(["in_transit", "at_warehouse", "delivered", "delayed"])
    }
    data.append(record)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("smart_tracking_data.csv", index=False)
df.to_json("smart_tracking_data.json", orient="records")

# Display first few rows
df.head()
