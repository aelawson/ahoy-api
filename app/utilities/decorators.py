
def handle_response(fn):
    def __wrapper(*args, **kwargs):
        fn(*args, **kwargs)
    return __wrapper
