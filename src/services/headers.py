class Headers:

    BASE_HEADERS = {
        'Content-Type': 'text/plain'
    }

    @classmethod
    def get_default_headers(cls, data):
        headers = dict(cls.BASE_HEADERS)
        headers['Content-Length'] = str(len(data))
        return cls.get_headers(headers)

    @classmethod
    def get_headers(cls, headers):
        if not headers:
            return cls.get_default_headers([])
        return [
            (header, value) for header, value in headers.items()
        ]
