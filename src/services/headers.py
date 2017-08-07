class Headers:

    BASE_HEADERS = [
        ('Content-Type', 'text/plain')
    ]

    @classmethod
    def get_default_headers(cls, data):
        return cls.BASE_HEADERS + [
            ('Content-Length', str(len(data)))
        ]

    @classmethod
    def get_headers(cls, headers):
        return [
            (header, value) for header, value in headers.items()
        ]
