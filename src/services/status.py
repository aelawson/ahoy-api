
class Status:

    STATUS_MAP = {
        200: {
            'status': '200 OK'
        },
        404: {
            'status': '404 Not Found'
        },
        500: {
            'status': '500 Internal Server Error'
        }
    }

    @classmethod
    def get_status_message(cls, status_code):
        return cls.STATUS_MAP.get(status_code, '')
