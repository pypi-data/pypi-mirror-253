from http import HTTPMethod
from http_api_lambda.models import ApiGatewayEvent

def build_example_event(route: str, method: HTTPMethod, body: str):
    return ApiGatewayEvent(
        version="2.0",
        route_key=f"{method} {route}",
        raw_path=route,
        raw_query_string="",
        headers=ApiGatewayEvent.Headers(
            accept="*/*",
            accept_encoding="gzip, deflate, br",
            content_length="",
            content_type="application/json",
            host="k3jkpitvf3.execute-api.eu-central-1.amazonaws.com"
        ),
        request_context=ApiGatewayEvent.RequestContext(
            account_id="",
            api_id="",
            domain_name="",
            domain_prefix="",
            http=ApiGatewayEvent.RequestContext.Http(
                method=method,
                path=route,
                protocol="HTTP/1.1",
                source_ip="",
                user_agent=""
            ),
            request_id="",
            route_key=f"{method} {route}",
            stage="$default",
            time="26/Nov/2023:16:56:04 +0000",
            timeEpoch= 1701017764971
        ),
        body=body,
        isBase64Encoded=False
    )