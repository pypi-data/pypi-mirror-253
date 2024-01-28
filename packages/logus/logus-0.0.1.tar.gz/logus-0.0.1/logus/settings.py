import os

LOG_LEVEL: str = os.environ.get("LOGUS_LOG_LEVEL", "")
LOG_JSON: bool = os.environ.get("LOGUS_LOG_JSON", "") == "true"
