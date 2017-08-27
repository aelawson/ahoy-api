
def handle_response(fn):
    def __decorator(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except NotImplementedError:
            return Response.response(405)
    return __decorator
