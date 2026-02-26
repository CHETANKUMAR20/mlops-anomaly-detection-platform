from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from anomaly_model import detect_anomalies

app = FastAPI(title="AI Log Anomaly Detection API")

class LogInput(BaseModel):
    cpu: int
    memory: int
    response_time: int

@app.get("/")
def root():
    return {"message": "AI Log Anomaly Detection Service Running"}

@app.post("/predict")
def predict(log: LogInput):
    df = pd.DataFrame([[log.cpu, log.memory, log.response_time]],
                      columns=["cpu", "memory", "response_time"])

    result = detect_anomalies(df)

    prediction = int(result["anomaly"].iloc[0])

    if prediction == -1:
        status = "ANOMALY DETECTED"
    else:
        status = "Normal"

    return {
        "cpu": log.cpu,
        "memory": log.memory,
        "response_time": log.response_time,
        "prediction": status
    }
