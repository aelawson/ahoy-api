from models.models import Release

from src.resource.base import BaseResource
from src.services.api import api
from src.services.db import db

@api.route('/teams/plans/releases/<release_id>/stage/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class StageResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        release_id = kwargs.get('release_id')
        release = Release.find(release_id).stage
        return {
            'status_code': 200,
            'body': release.serialize()
        }
