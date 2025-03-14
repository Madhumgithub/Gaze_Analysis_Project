import pandas as pd
import numpy as np
import os

# Ensure the datasets folder exists
os.makedirs("datasets", exist_ok=True)

# Generate fake gaze data
data = {
    "timestamp": np.arange(100),
    "x": np.random.randint(100, 500, 100),
    "y": np.random.randint(100, 500, 100),
    "pupil_diameter": np.random.rand(100) * 5 + 2  # Random values for pupil size
}

df = pd.DataFrame(data)

# Save the CSV inside datasets/
df.to_csv("datasets/gaze_data.csv", index=False)

print("✅ Fake gaze data generated and saved to datasets/gaze_data.csv!")
