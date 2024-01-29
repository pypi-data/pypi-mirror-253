from typing import Any, Callable, Dict, NewType

Serialazable = Any

LogAttrs = Dict[str, Serialazable]
LogType = Callable[[LogAttrs], None]


LibName = NewType("LibName", str)
LogLevel = NewType("LogLevel", int)
RootLogLevel = NewType("RootLogLevel", int)
