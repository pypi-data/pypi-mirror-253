import os

LOG_LEVEL: str = os.environ.get("TYPELOG_LOG_LEVEL", "")
LOG_JSON: bool = os.environ.get("TYPELOG_LOG_JSON", "") == "true"

add_thread: bool = os.environ.get("TYPELOG_ADD_THREAD") == "true"
add_process: bool = os.environ.get("TYPELOG_ADD_PROCESS") == "true"
add_level: bool = os.environ.get("TYPELOG_ADD_LEVEL") == "true"
add_filepath: bool = os.environ.get("TYPELOG_ADD_FILEPATH") == "true"
add_time: bool = os.environ.get("TYPELOG_ADD_TIME") == "true"
