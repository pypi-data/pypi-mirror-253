from typing import Any, Callable, Dict, NewType

LogAttrs = NewType("LogAttrs", Dict[str, Any])
LogType = Callable[[LogAttrs], None]
