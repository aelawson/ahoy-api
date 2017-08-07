from src.services.api import api
from src.services.response import Response

def application(env, start_response):

    try:
        return api.handle_request(start_response, env)
    except:
        return Response.response(start_response, status_code=500)
