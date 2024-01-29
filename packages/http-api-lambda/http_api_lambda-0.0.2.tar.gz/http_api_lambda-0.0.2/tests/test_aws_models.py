# test the validity of the AWS models like ApiGatewayEvent and LambdaContext

from http_api_lambda.models import ApiGatewayEvent

example_event = {'version': '2.0',
     'routeKey': '$default',
     'rawPath': '/favicon.ico',
     'rawQueryString': '',
     'cookies': ['awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiNWY5NWE5NTAtZTM3NC00N2MxLTg1ODctYzNmOWM0YmVmMjFjIiwidiI6IjEifQ=='],
     'headers': {'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,sv;q=0.6',
                 'content-length': '0', 'host': 'abc.execute-api.eu-central-1.amazonaws.com',
                 'referer': 'https://abc.execute-api.eu-central-1.amazonaws.com/',
                 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?0',
                 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'image', 'sec-fetch-mode': 'no-cors', 'sec-fetch-site': 'same-origin',
                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                 'x-amzn-trace-id': 'Root=1-65b636b9-3f4bd65938b6b12a29e4e640', 'x-forwarded-for': '93.204.208.51', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'},
     'requestContext': {'accountId': '482228791258',
                        'apiId': '2dq0aytptk',
                        'domainName': '2dq0aytptk.execute-api.eu-central-1.amazonaws.com',
                        'domainPrefix': '2dq0aytptk',
                        'http': {'method': 'GET',
                                 'path': '/favicon.ico',
                                 'protocol': 'HTTP/1.1',
                                 'sourceIp': '93.204.208.51',
                                 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'},
                        'requestId': 'SP18-izXFiAEMjg=',
                        'routeKey': '$default',
                        'stage': '$default',
                        'time': '28/Jan/2024:11:12:57 +0000',
                        'timeEpoch': 1706440377191},
     'isBase64Encoded': False}

def test_validate_api_gateway_event():
    ApiGatewayEvent.model_validate(example_event)