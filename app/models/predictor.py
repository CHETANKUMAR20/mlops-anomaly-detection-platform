import joblib
import pandas as pd
import os

from app.core.metrics import REQUEST_COUNT, ANOMALY_COUNT, REQUEST_LATENCY
import time
from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

if not os.path.exists(settings.MODEL_PATH):
    raise Exception("Model not found. Run training first.")

model = joblib.load(settings.MODEL_PATH)

logger.info("Model loaded successfully.")

def predict(cpu, memory, response_time):

    start_time = time.time()
    REQUEST_COUNT.inc()

    df = pd.DataFrame([[cpu, memory, response_time]],
                      columns=["cpu", "memory", "response_time"])

    prediction = model.predict(df)[0]

    result = "ANOMALY DETECTED" if prediction == -1 else "Normal"

    if prediction == -1:
        ANOMALY_COUNT.inc()

    REQUEST_LATENCY.observe(time.time() - start_time)

    logger.info(
        f"Prediction made | CPU={cpu} MEM={memory} RESP={response_time} RESULT={result}"
    )

    return result
