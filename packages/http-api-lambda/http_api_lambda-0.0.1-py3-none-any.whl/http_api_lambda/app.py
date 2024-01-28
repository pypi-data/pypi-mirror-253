from http import HTTPMethod
from pydantic import BaseModel
from typing import get_type_hints

from http_api_lambda.core import Handler, RouterBase
from http_api_lambda.models import ApiGatewayEvent, LambdaContext, Response
from http_api_lambda.router import Router
from http_api_lambda.exceptions import HTTPException

class App(RouterBase):
    def _lookup_handler(self, route: str, method: HTTPMethod) -> Handler:
        for handler in self.handlers:
            if handler.method == method and handler.route_pattern.match(route):
                return handler
        raise Exception("Handler not found")
    
    def _build_decorator(self, route: str, method: HTTPMethod, success_status_code: int):
        def decorator(f):
            self.handlers.append(
                Handler(route=route, method=method, success_status_code=success_status_code, handler_fn=f))
            return RouterBase._build_wrapper(f)
        return decorator

    @staticmethod
    def _cast_arguments(route: str, event: ApiGatewayEvent, context, handler: Handler) -> list:
        """Invoked with data from the request, casts the arguments to the correct type the handler expects"""
        arguments: dict = get_type_hints(handler.handler_fn)
        arguments.pop("return", ModuleNotFoundError)

        casted_args = []
        for arg, t in arguments.items():
            if t == LambdaContext:
                casted_args.append(context)
            elif t == ApiGatewayEvent:
                casted_args.append(event)
            elif issubclass(t, BaseModel):
                casted_args.append(t.model_validate_json(event.body))
            elif arg in handler.path_params:
                casted_args.append(
                    t(handler.route_pattern.match(route).group(arg)))
            else:
                continue

        return casted_args
    
    @staticmethod
    def _invoke_handler(handler: Handler, casted_args: list) -> Response:
        type_hints = get_type_hints(handler.handler_fn)
        return_type = type_hints.get("return", None)
        
        try:
            handler_response: BaseModel = handler.handler_fn(*casted_args)
        except HTTPException as e:
            return Response(
                status_code=e.status_code,
                body=e.message
            )

        if return_type == None:
            return Response(
                statusCode=handler.success_status_code,
                body=str(handler_response)
            )
        elif issubclass(return_type, BaseModel):
            return Response(
                statusCode=handler.success_status_code,
                body=return_type.model_validate(handler_response).model_dump_json()
            )
    
    def handle_request(self, event: dict, context) -> str:
        """This is the AWS Lambda entrypoint"""
        event: ApiGatewayEvent = ApiGatewayEvent.model_validate(event)
        route = event.request_context.http.path
        method = event.request_context.http.method

        # lookup correct handler
        handler = self._lookup_handler(route, method)
        casted_args = self._cast_arguments(route, event, context, handler)

        response = self._invoke_handler(handler, casted_args)
        return response.model_dump(by_alias=True)
        
    
    def include_router(self, router: Router):
        self.handlers.extend(router.handlers)