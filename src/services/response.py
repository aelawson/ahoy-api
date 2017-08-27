import json

from src.services.headers import Headers
from src.services.status import Status

class Response:

    @classmethod
    def response(cls, start_response, status_code=200, headers=None, body=''):
        headers = Headers.construct_headers(headers)
        status = Status.get_status_message(status_code)
        start_response(
            status,
            headers
        )
        return [body.encode('utf-8')]
