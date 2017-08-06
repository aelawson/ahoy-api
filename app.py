from src.services.api import Api
from src.services.response import Response

def application(env, start_response):

    response = Response(status_code=200)
    response.set_body(b'Hello World!')
    start_response(
        response.status['status'],
        response.headers
    )
    return [response.body]
