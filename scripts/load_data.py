import pandas as pd

def load_gaze_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Example usage
if __name__ == "__main__":
    gaze_df = load_gaze_data("../datasets/gaze_data.csv")
    print(gaze_df.head())
