from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from app.schemas.log_schema import LogInput
from app.models.predictor import predict
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def readiness():
    return {"status": "ready"}

@app.post("/predict")
def detect(log: LogInput):
    result = predict(log.cpu, log.memory, log.response_time)
    return {
        "cpu": log.cpu,
        "memory": log.memory,
        "response_time": log.response_time,
        "prediction": result
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
