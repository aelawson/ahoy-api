from models.models import Plan, Release

from src.resource.base import BaseResource
from src.services.api import api
from src.services.db import db

@api.route('/teams/plans/<plan_id>/releases/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class ReleasesResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        plan_id = kwargs.get('plan_id')
        releases = Plan.find(plan_id).releases
        return {
            'status_code': 200,
            'body': releases.serialize()
        }

@api.route('/teams/plans/releases/<release_id>/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class ReleaseResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        release_id = kwargs.get('release_id')
        release = Release.find(release_id)
        return {
            'status_code': 200,
            'body': release.serialize()
        }
