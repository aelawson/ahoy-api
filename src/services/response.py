import json

from src.services.headers import Headers
from src.services.status_codes import StatusCodes

class Response:

    def __init__(self, status_code=200, headers=None, body=b''):
        if not headers:
            self.headers = Headers.get_default_headers(body)
        else:
            self.headers = headers
        self.body = body
        self.status = StatusCodes.get_status_message(status_code)

    def set_status(self, status_code):
        self.status = StatusCodes.get_status_message(status_code)

    def set_body(self, body):
        self.body = body
        self.headers = Headers.get_default_headers(body)
