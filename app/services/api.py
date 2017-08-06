
class Api:

    def __init__(self):
        self.routes = {}

    def route(self, route):
        def __decorator(fn):
            self.routes[route] = fn
            return fn
        return __decorator
