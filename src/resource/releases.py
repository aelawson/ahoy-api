from models.models import Plan, Release, Stage

from src.resource.base import BaseResource
from src.services.api import api
from src.services.db import db
from src.services.release import ReleaseService

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

@api.route('/teams/plans/releases/<release_id>/cut/')
@api.methods(['HEAD', 'OPTIONS', 'POST'])
class CutActionResource(BaseResource):

    @api.json
    def post(*args, **kwargs):
        release_id = kwargs.get('release_id')
        major = kwargs.get('major')
        minor = kwargs.get('minor')
        patch = kwargs.get('patch')

        release = Release.find(release_id)

        try:
            ReleaseService.cut(release, major, minor, patch)
        except Exception as e:
            raise e

        next_stage = Stage.where('name', '=', 'Staging').first()
        release.stage_id = next_stage.id
        release.save()

        return {
            'status_code': 200
        }

@api.route('/teams/plans/releases/<release_id>/release/')
@api.methods(['HEAD', 'OPTIONS', 'POST'])
class ReleaseActionResource(BaseResource):

    @api.json
    def post(*args, **kwargs):
        release_id = kwargs.get('release_id')

        release = Release.find(release_id)

        try:
            ReleaseService.release(release)
        except Exception as e:
            raise e

        next_stage = Stage.where('name', '=', 'Production').first()
        release.stage_id = next_stage.id
        release.save()

        return {
            'status_code': 200
        }
