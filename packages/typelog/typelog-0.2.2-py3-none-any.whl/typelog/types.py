from typing import Any, Callable, Dict, NewType

LogAttrs = NewType("LogAttrs", Dict[str, Any])
LogType = Callable[[LogAttrs], None]


LibName = NewType("LibName", str)
LogLevel = NewType("LogLevel", int)
RootLogLevel = NewType("RootLogLevel", int)

Serialazable = Any
