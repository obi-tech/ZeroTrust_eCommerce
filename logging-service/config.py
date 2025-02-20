import os

class Config:
    # Database settings
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/account_management")
    
    # Server settings
    GRPC_PORT = int(os.getenv("GRPC_PORT", "50055"))
    API_PORT = int(os.getenv("API_PORT", "8000"))
    
    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Metrics settings
    METRICS_ENABLED = os.getenv("METRICS_ENABLED", "true").lower() == "true"
    METRICS_UPDATE_INTERVAL = int(os.getenv("METRICS_UPDATE_INTERVAL", "60"))  # seconds
