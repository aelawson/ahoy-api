class Headers:

    DEFAULT_HEADERS = {
        'Content-Type': 'text/plain'
    }

    @classmethod
    def construct_headers(cls, headers, body=''):
        if not headers:
            headers = cls.DEFAULT_HEADERS
        headers['Content-Length'] = str(len(body))
        return [
            (header, value) for header, value in headers.items()
        ]
