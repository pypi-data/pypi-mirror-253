from .logtypes import LogOption, LogParams


def Error(value: Exception) -> LogOption:
    def add_option(params: LogParams) -> None:
        params["error"] = str(value)
        params["error_type"] = type(value)

    return add_option


def String(key: str, value: str) -> LogOption:
    def add_option(params: LogParams) -> None:
        params[key] = value

    return add_option


def Int(key: str, value: int) -> LogOption:
    def add_option(params: LogParams) -> None:
        params[key] = value

    return add_option


def Float(key: str, value: float) -> LogOption:
    def add_option(params: LogParams) -> None:
        params[key] = value

    return add_option
