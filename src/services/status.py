
class Status:

    STATUS_MAP = {
        200: '200 OK',
        404: '404 Not Found',
        405: '405 Method Not Allowed',
        500: '500 Internal Server Error'
    }

    @classmethod
    def get_status_message(cls, status_code):
        return cls.STATUS_MAP.get(status_code, '')
