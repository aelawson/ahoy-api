
def handle_response(fn):
    def __decorator(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except NotImplementedError:
            return Response.response(405)
    return __decorator

def header(self, header, value):
    def __decorator(fn):
        response = fn(*args, **kwargs)
        response['headers'][header] = value
        return response
    return __decorator