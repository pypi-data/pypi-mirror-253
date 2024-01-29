from typing import Any, Callable, Dict

Serialazable = Any
LogAttrs = Dict[str, Serialazable]
LogType = Callable[[LogAttrs], None]
LibName = str
LogLevel = int
RootLogLevel = LogLevel
