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
    def get_handler(self):
        self.get()

    @handle_response
    def post_handler(self):
        self.post()

    @handle_response
    def put_handler(self):
        self.put()

    @handle_response
    def patch_handler(self):
        self.patch()

    @handle_response
    def delete_handler(self):
        self.delete()
