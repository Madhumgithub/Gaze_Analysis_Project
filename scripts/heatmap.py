import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import os

def create_gaze_heatmap(df, save_path):
    """Generate a heatmap of gaze fixations."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure folder exists

    img_size = (500, 500)
    heatmap = np.zeros(img_size, dtype=np.float32)

    for _, row in df.iterrows():
        x, y = int(row["x"]), int(row["y"])
        heatmap[y % img_size[1], x % img_size[0]] += 1

    heatmap = cv2.GaussianBlur(heatmap, (25, 25), 10)

    plt.figure(figsize=(6,6))
    sns.heatmap(heatmap, cmap="jet", cbar=True)
    plt.title("Gaze Heatmap")
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Gaze Heatmap saved at {save_path}")

def create_gaze_grid_heatmap(df, save_path, grid_size=10):
    """Generate a heatmap by dividing the image into grid cells."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure folder exists

    img_size = (500, 500)
    heatmap = np.zeros((grid_size, grid_size), dtype=np.float32)

    for _, row in df.iterrows():
        x, y = row["x"], row["y"]
        grid_x = int((x / img_size[0]) * grid_size)
        grid_y = int((y / img_size[1]) * grid_size)
        heatmap[grid_y, grid_x] += 1

    plt.figure(figsize=(6,6))
    plt.imshow(heatmap, cmap="jet", interpolation="nearest")
    plt.title("Gaze Grid Heatmap")
    plt.colorbar(label="Fixation Count")
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Gaze Grid Heatmap saved at {save_path}")

if __name__ == "__main__":
    df = pd.read_csv("../datasets/gaze_data.csv")
    create_gaze_heatmap(df, "../heatmaps/gaze_heatmap.png")
    create_gaze_grid_heatmap(df, "../heatmaps/gaze_grid_heatmap.png")
