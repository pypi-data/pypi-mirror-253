import os

LOG_LEVEL: str = os.environ.get("TYPELOG_LOG_LEVEL", "")
LOG_JSON: bool = os.environ.get("TYPELOG_LOG_JSON", "") == "true"
