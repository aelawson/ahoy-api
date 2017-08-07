from src.services.response import Response

class Api:

    def __init__(self):
        self.routes = {}

    def handle_request(self, start_response, env):
        method = env.get('REQUEST_METHOD')
        query = env.get('QUERY_STRING')
        path = env.get('RAW_URI')
        params = None

        resource = self.routes.get(path)
        if resource:
            method_handler = getattr(
                resource,
                '{method}_handler'.format(method=method.lower())
            )
            response_data = method_handler(query, params)
            return Response.response(
                start_response,
                status_code=response_data.get('status_code'),
                headers=response_data.get('headers'),
                body=response_data.get('body')
            )
        else:
            return Response.response(start_response, 404)

    def route(self, route):
        def __decorator(cls):
            self.routes[route] = cls()
            return cls
        return __decorator

api = Api()
