from src.utilities.decorators import handle_response
from src.utilities.exceptions import MethodNotImplementedException

class BaseResource:

    # Overridable Hooks

    def get(self):
        raise MethodNotImplementedException

    def post(self):
        raise MethodNotImplementedException

    def put(self):
        raise MethodNotImplementedException

    def patch(self):
        raise MethodNotImplementedException

    def delete(self):
        raise MethodNotImplementedException

    # HTTP Method Handlers

    @handle_response
    def get_handler(self, *args, **kwargs):
        return self.get(*args, **kwargs)

    @handle_response
    def post_handler(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @handle_response
    def put_handler(self, *args, **kwargs):
        return self.put(*args, **kwargs)

    @handle_response
    def patch_handler(self, *args, **kwargs):
        return self.patch(*args, **kwargs)

    @handle_response
    def delete_handler(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
