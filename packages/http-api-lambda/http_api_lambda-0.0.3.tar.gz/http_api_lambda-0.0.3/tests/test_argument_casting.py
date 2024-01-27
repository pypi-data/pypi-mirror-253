from http import HTTPMethod
from http_api_lambda.app import Handler, App
from http_api_lambda.models import ApiGatewayEvent, LambdaContext
from pydantic import BaseModel
from tests.data.example_api_gateway_events import build_example_event


class User(BaseModel):
    id: int
    name: str

def test_cast_arguments():
    def handler_fn(user_id: int, user: User, event: ApiGatewayEvent, context: LambdaContext):
        pass
    
    handler = Handler(route="/users/{user_id}", method=HTTPMethod.GET, success_status_code=200, handler_fn=handler_fn)
    example_event = build_example_event(route="/users/123", method=HTTPMethod.GET, body='{"id": 123, "name": "John Doe"}')

    args = App._cast_arguments(route="/users/123", event=example_event, context=None, handler=handler)
    assert args == [123, User(id=123, name="John Doe"), example_event, None]