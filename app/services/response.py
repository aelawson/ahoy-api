import json

class Response:

    RESPONSE_MAP = {
        200: {
            'status': '200 OK'
        }
    }

    def __init__(self, status=200, headers=[], body={}):
        self.body = body,
        self.headers = headers,
        self.status = self.__class__.RESPONSE_MAP.get(status)

    def set_status(self, status):
        self.status = self.__class__.RESPONSE_MAP.get(status)
