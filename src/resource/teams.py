from models.models import Team

from src.resource.base import BaseResource
from src.services.api import api
from src.services.db import db

@api.route('/teams/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class TeamsResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        teams = Team.all()
        return {
            'status_code': 200,
            'body': teams.serialize()
        }

@api.route('/teams/<id>/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class TeamResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        team_id = kwargs.get('id')
        if team_id:
            team = Team.where('id', team_id).get()
            return {
                'status_code': 200,
                'body': team.serialize()
            }
        else:
            return {
                'status_code': 405
            }
            