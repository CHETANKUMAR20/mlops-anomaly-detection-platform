import os

class Settings:
    APP_NAME: str = "AI Infrastructure Monitoring System"
    VERSION: str = "1.0.0"
    MODEL_PATH: str = os.getenv(
        "MODEL_PATH", 
        os.path.join("app", "models", "model.joblib")
    )

settings = Settings()
