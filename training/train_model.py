import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = "app/models/model.joblib"

def train():

    # Simulated baseline normal server behaviour
    baseline_data = pd.DataFrame([
        [30, 40, 120],
        [35, 45, 110],
        [32, 38, 130],
        [28, 41, 100],
        [29, 39, 115],
        [31, 42, 118],
        [34, 44, 122]
    ], columns=["cpu", "memory", "response_time"])

    model = IsolationForest(contamination=0.15, random_state=42)
    model.fit(baseline_data)

    os.makedirs("app/models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("✅ Model trained and saved at:", MODEL_PATH)

if __name__ == "__main__":
    train()
