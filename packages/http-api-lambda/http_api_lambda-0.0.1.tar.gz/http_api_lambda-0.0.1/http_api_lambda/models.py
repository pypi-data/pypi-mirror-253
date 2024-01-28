from pydantic import BaseModel, Field, ConfigDict

class ApiGatewayEvent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    class Headers(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        accept: str
        accept_encoding: str = Field(alias='accept-encoding')
        content_length: str = Field(alias='content-length')
        content_type: str = Field(alias='content-type')
        host: str | None
    
    class RequestContext(BaseModel):
        model_config = ConfigDict(populate_by_name=True)
        class Http(BaseModel):
            model_config = ConfigDict(populate_by_name=True)
            method: str
            path: str
            protocol: str
            source_ip: str = Field(alias='sourceIp')
            user_agent: str = Field(alias='userAgent')
            
        account_id: str = Field(alias='accountId')
        api_id: str = Field(alias='apiId')
        domain_name: str = Field(alias='domainName')
        domain_prefix: str = Field(alias='domainPrefix')        
        http: Http
        request_id: str = Field(alias='requestId')
        route_key: str = Field(alias='routeKey')
        stage: str
        time: str
        time_epoch: int = Field(alias='timeEpoch')
        
    version: str
    route_key: str = Field(alias='routeKey')
    raw_path: str = Field(alias='rawPath')
    raw_query_string: str = Field(alias='rawQueryString')
    headers: Headers
    request_context: RequestContext = Field(alias='requestContext')
    body: str
    is_base64_encoded: bool = Field(alias='isBase64Encoded')
    
    
class LambdaContext(BaseModel):
    function_name: str
    function_version: str
    invoked_function_arn: str
    memory_limit_in_mb: int
    aws_request_id: str
    log_group_name: str
    log_stream_name: str


class Response(BaseModel):
    is_base64_encoded: bool = Field(alias='isBase64Encoded', default=False)
    status_code: int = Field(alias='statusCode', default=200)
    body: str = ''
    headers: dict = {}