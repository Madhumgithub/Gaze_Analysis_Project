import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_gaze_sequence(df):
    # Sort by timestamp to maintain sequence order
    df = df.sort_values(by="timestamp")

    # Create sequence ID for each point
    df["sequence_id"] = np.arange(len(df))

    return df

if __name__ == "__main__":
    df = pd.read_csv("datasets/gaze_data.csv")
    df = compute_gaze_sequence(df)
    
    print(df.head())  # Check the new sequence IDs
    df.to_csv("datasets/gaze_sequence.csv", index=False)  # Save processed data
