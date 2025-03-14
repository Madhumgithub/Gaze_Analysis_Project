import numpy as np
import pandas as pd

def compute_saccade_features(df):
    """Calculate saccade offsets and distances."""
    if "x" in df.columns and "y" in df.columns:
        x = df["x"].values
        y = df["y"].values
    else:
        x = df["X_Coordinate"].values
        y = df["Y_Coordinate"].values

    so_x = np.diff(x)  # Horizontal offset
    so_y = np.diff(y)  # Vertical offset
    sd = np.sqrt(so_x**2 + so_y**2)  # Euclidean distance

    return so_x, so_y, sd

def clean_gaze_data(df):
    """Remove unnecessary gaze points (first/last, short-duration, center)."""
    df = df.iloc[2:-2]  # Remove first and last 2 gaze points
    df = df[df["pupil_diameter"] > 3]  # Remove short-duration gazes
    center_x, center_y = 250, 250  # Assuming 500x500 image
    df = df[((df["x"] - center_x) ** 2 + (df["y"] - center_y) ** 2) > 10000]  

    return df

if __name__ == "__main__":
    df = pd.read_csv("../datasets/gaze_data.csv")
    df = clean_gaze_data(df)
    df.to_csv("../datasets/cleaned_gaze_data.csv", index=False)
    print("✅ Cleaned gaze data saved to datasets/cleaned_gaze_data.csv")
