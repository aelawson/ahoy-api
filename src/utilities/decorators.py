
def handle_response(fn):
    def __wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return __wrapper
