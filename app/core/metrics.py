from prometheus_client import Counter, Histogram

# Total API requests
REQUEST_COUNT = Counter(
    "ai_requests_total",
    "Total number of prediction requests"
)

# Total anomalies detected
ANOMALY_COUNT = Counter(
    "ai_anomalies_total",
    "Total number of anomalies detected"
)

# Request latency
REQUEST_LATENCY = Histogram(
    "ai_request_latency_seconds",
    "Time spent processing prediction requests"
)
