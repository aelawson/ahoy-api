from src.utilities.decorators import handle_response

class BaseResource:

    # Overridable Hooks

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError

    def patch(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

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
