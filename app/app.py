from services.response import Response

def application(env, start_response):
    response = Response(status=200)
    response.body = b'Hello World!'
    start_response(
        response.status['status'],
        response.headers
    )
    return [response.body]
