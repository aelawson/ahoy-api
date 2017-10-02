import json
import re

from src.services.response import Response
from src.utilities.exceptions import InvalidRouteFormatException

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

    @classmethod
    def build_route_pattern(cls, route):
        if re.match(r'^/([<>_\w]+/)*$', route):
            route_pattern = re.sub(
                r'(<\w+>)/',
                r'(?:(?<=/)(?:(?P\1[^<>/])/))',
                route
            )
            if route_pattern != route:
                route_pattern += '?'
            return re.compile("^{pattern}$".format(pattern=route_pattern))
        else:
            raise InvalidRouteFormatException

    def __init__(self):
        self.routes = []
        self.resources = {}

    def handle_request(self, start_response, env):
        method = env.get('REQUEST_METHOD')
        query = env.get('QUERY_STRING')
        path = env.get('RAW_URI')

        route_match = self.match_route(path)

        if route_match:
            resource, params = route_match
            methods = self.resources[type(resource).__name__].get('methods')
            if not methods or method not in methods:
                return Response.response(
                    start_response,
                    status_code=405
                )

            if method == 'OPTIONS':
                headers = {
                    'Allow' : ', '.join(methods)
                }
                return Response.response(
                    start_response,
                    headers=headers
                )
            elif method == 'HEAD':
                # Hacky way to ensure we've initialized GET headers (for now)
                get_handler = getattr(resource, 'get_handler')
                response_data = get_handler(query, params)
                resource_methods = self.resources[type(resource).__name__]['methods']
                return Response.response(
                    start_response,
                    headers=response_data.get('headers')
                )

            method_handler = getattr(
                resource,
                '{method}_handler'.format(method=method.lower())
            )

            response_data = method_handler(query, **params)
            return Response.response(
                start_response,
                status_code=response_data.get('status_code'),
                headers=response_data.get('headers'),
                body=response_data.get('body', '')
            )
        else:
            return Response.response(
                start_response,
                status_code=404
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
            pattern = self.__class__.build_route_pattern(route)
            self.routes.append({
                'pattern': pattern,
                'resource': cls()
            })
            return cls
        return __decorator

    def match_route(self, path):
        for route in self.routes:
            match = re.match(route['pattern'], path)
            if match:
                return route['resource'], match.groupdict()

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
        if not response.get('headers'):
            response['headers'] = {}
        response['headers'][header] = value
        return response

api = Api()
