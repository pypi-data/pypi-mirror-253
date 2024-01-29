from . import settings as settings, types as types
from _typeshed import Incomplete

is_configured: bool

class LogConfig:
    lib_name: Incomplete
    log_level: Incomplete
    def __init__(self, lib_name: types.LibName, log_level: types.LogLevel) -> None: ...

class Loggers:
    root_log_level: Incomplete
    log_configs: Incomplete
    turn_json: Incomplete
    add_thread: Incomplete
    add_process: Incomplete
    add_level: Incomplete
    add_filepath: Incomplete
    add_time: Incomplete
    def __init__(self, root_log_level: types.RootLogLevel, *log_configs: LogConfig, turn_json: bool = ..., add_thread: bool = ..., add_process: bool = ..., add_level: bool = ..., add_filepath: bool = ..., add_time: bool = ...) -> None: ...
    def configure(self) -> None: ...
