from src.resource.base import BaseResource
from src.services.api import api

@api.route('/test/path')
class TestResource(BaseResource):

    def get(*args, **kwargs):
        return {
            'status_code': 200,
            'body': b'Successful GET Request',
            'headers': {
                'Content-Type': 'application/json'
            }
        }
