
class StatusCodes:

    STATUS_MAP = {
        200: {
            'status': '200 OK'
        }
    }

    @classmethod
    def get_status_message(cls, code):
        return cls.STATUS_MAP.get(code, '')
