from http import HTTPMethod
from http_api_lambda.core import Handler, RouterBase


class Router(RouterBase):
    def __init__(self, route_prefix = "") -> None:
        super().__init__()
        self.route_prefix = route_prefix

    def _build_decorator(self, route: str, method: HTTPMethod, success_status_code: int):
        def decorator(f):
            self.handlers.append(
                Handler(route=self.route_prefix + route, method=method, success_status_code=success_status_code, handler_fn=f))
            return RouterBase._build_wrapper(f)
        return decorator