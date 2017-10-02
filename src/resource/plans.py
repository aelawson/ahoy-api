from models.models import Team, Plan

from src.resource.base import BaseResource
from src.services.api import api
from src.services.db import db

@api.route('/teams/<team_id>/plans/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class PlansResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        team_id = kwargs.get('team_id')
        plans = Team.find(team_id).plan
        return {
            'status_code': 200,
            'body': plans.serialize()
        }

@api.route('/teams/plans/<plan_id>/')
@api.methods(['HEAD', 'OPTIONS', 'GET'])
class PlanResource(BaseResource):

    @api.json
    def get(*args, **kwargs):
        plan_id = kwargs.get('plan_id')
        plan = Plan.find(plan_id)
        return {
            'status_code': 200,
            'body': plan.serialize()
        }
