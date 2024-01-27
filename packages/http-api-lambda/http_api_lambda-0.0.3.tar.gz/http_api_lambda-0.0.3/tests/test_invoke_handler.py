from pydantic import BaseModel
from http_api_lambda import App
from http_api_lambda.core import Handler
from http import HTTPMethod

class UserOut(BaseModel):
    name: str

def test_handler_invocation():
    def get_users() -> UserOut:
        return {"id": 1, "name": "test"}
    
    handler = Handler(
        route="/users/{id}",
        method=HTTPMethod.GET,
        success_status_code=200,
        handler_fn=get_users
    )

    response = App._invoke_handler(handler, [])
    
    assert response.status_code == 200