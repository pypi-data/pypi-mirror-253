from .types import LogAttrs, LogType


def Error(value: Exception) -> LogType:
    def add_option(params: LogAttrs) -> None:
        params["error"] = str(value)
        params["error_type"] = type(value)

    return add_option


def String(key: str, value: str) -> LogType:
    def add_option(params: LogAttrs) -> None:
        params[key] = value

    return add_option


def Int(key: str, value: int) -> LogType:
    def add_option(params: LogAttrs) -> None:
        params[key] = value

    return add_option


def Float(key: str, value: float) -> LogType:
    def add_option(params: LogAttrs) -> None:
        params[key] = value

    return add_option
