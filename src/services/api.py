import json

from src.services.response import Response

class Api:

    METHODS = [
        'OPTIONS',
        'HEAD',
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE'
    ]

    def __init__(self):
        self.routes = {}
        self.resources = {}

    def handle_request(self, start_response, env):
        method = env.get('REQUEST_METHOD')
        query = env.get('QUERY_STRING')
        path = env.get('RAW_URI')
        params = None

        resource = self.routes.get(path)

        if resource:
            methods = self.resources[type(resource).__name__]['methods']
            if not methods or method not in methods:
                return Response.response(
                    start_response,
                    status_code=405
                )

            if method == 'OPTIONS':
                headers = { 'Allow' : ', '.join(methods) }
                return Response.response(
                    start_response,
                    status_code=200,
                    headers=headers
                )
            if method == 'HEAD':
                # Hacky way to ensure we've initialized GET headers (for now)
                get_handler = getattr(resource, 'get_handler')
                response_data = get_handler(query, params)
                resource_methods = self.resources[type(resource).__name__]['methods']
                return Response.response(
                    start_response,
                    status_code=200,
                    headers=response_data.get('headers')
                )

            method_handler = getattr(
                resource,
                '{method}_handler'.format(method=method.lower())
            )

            response_data = method_handler(query, params)
            body = response_data.get('body', '')
            return Response.response(
                start_response,
                status_code=response_data.get('status'),
                headers=response_data.get('headers'),
                body=body
            )
        else:
            return Response.response(
                start_response,
                404
             )

    def methods(self, route_methods):
        def __decorator(cls):
            self.resources[cls.__name__] = {
                'methods': []
            }
            methods = route_methods
            if methods == '*':
                methods = self.__class__.METHODS
            for method in methods:
                self.resources[cls.__name__]['methods'].append(method.upper())
            return cls
        return __decorator

    def route(self, route):
        def __decorator(cls):
            self.routes[route] = cls()
            return cls
        return __decorator

    # Headers

    def header(self, header, value):
        def __wrapper(fn):
            def __decorator(*args, **kwargs):
                response = fn(*args, **kwargs)
                return self._add_header(response, header, value)
            return __decorator
        return __wrapper

    def json(self, fn):
        def __decorator(*args, **kwargs):
            response = fn(*args, **kwargs)
            response['body'] = json.dumps(response.get('body', ''))
            return self._add_header(response, 'Content-Type', 'application/json')
        return __decorator

    def _add_header(self, response, header, value):
        print(response)
        if not response.get('headers'):
            response['headers'] = {}
        response['headers'][header] = value
        return response

api = Api()
