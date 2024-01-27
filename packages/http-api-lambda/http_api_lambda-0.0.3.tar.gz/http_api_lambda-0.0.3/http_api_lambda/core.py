from http import HTTPMethod
from abc import ABC, abstractmethod
import re
from typing import Callable


class Handler:
    """Class to store additional information about the handler function"""

    def __init__(self, route: str, method: HTTPMethod, success_status_code: int, handler_fn: Callable) -> None:
        self.method = method
        self.success_status_code = success_status_code
        self.handler_fn = handler_fn

        # Build a regex pattern from the route definition
        self.route_pattern = re.compile(
            "^" + route.replace("{", "(?P<").replace("}", ">[^/]*)") + "$")

        # Analyze the route definition and store a list of path parameters
        self.path_params = re.findall(r"{(\w+)}", route)


class RouterBase(ABC):
    def __init__(self) -> None:
        self.handlers: list[Handler] = []

    @staticmethod
    def _build_wrapper(f):
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
        return wrapper

    @abstractmethod
    def _build_decorator(self, route: str, method: HTTPMethod, success_status_code: int):
        pass

    # Decorators
    def get(self, route: str, success_status_code: int = 200):
        return self._build_decorator(route=route, method=HTTPMethod.GET, success_status_code=success_status_code)

    def put(self, route: str, success_status_code: int = 200):
        return self._build_decorator(route=route, method=HTTPMethod.PUT, success_status_code=success_status_code)

    def post(self, route: str, success_status_code: int = 200):
        return self._build_decorator(route=route, method=HTTPMethod.POST, success_status_code=success_status_code)

    def delete(self, route: str, success_status_code: int = 200):
        return self._build_decorator(route=route, method=HTTPMethod.DELETE, success_status_code=success_status_code)
