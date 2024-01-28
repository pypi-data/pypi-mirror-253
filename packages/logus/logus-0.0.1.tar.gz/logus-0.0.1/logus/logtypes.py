from typing import Any, Callable, Dict, NewType

LogParams = NewType("LogParams", Dict[str, Any])
LogOption = Callable[[LogParams], None]
