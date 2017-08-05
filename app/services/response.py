import json

class Response:

    RESPONSE_MAP = {
        200: {
            'status': '200 OK'
        }
    }
    DEFAULT_HEADERS = [
        ('Content-Type', 'text/plain')
    ]

    def __init__(self, status=200, headers=None, body={}):
        if not headers:
            self.headers = self.__class__.DEFAULT_HEADERS
        else:
            self.headers = headers
        self.body = body,
        self.status = self.__class__.RESPONSE_MAP.get(status)

    def set_status(self, status):
        self.status = self.__class__.RESPONSE_MAP.get(status)
