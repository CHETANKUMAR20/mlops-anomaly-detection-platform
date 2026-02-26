from sklearn.ensemble import IsolationForest
import pandas as pd

# Train model once with baseline normal behavior
baseline_data = pd.DataFrame([
    [30, 40, 120],
    [35, 45, 110],
    [32, 38, 130],
    [28, 41, 100]
], columns=["cpu", "memory", "response_time"])

model = IsolationForest(contamination=0.2, random_state=42)
model.fit(baseline_data)

def detect_anomalies(df):
    df["anomaly"] = model.predict(df)
    return df
