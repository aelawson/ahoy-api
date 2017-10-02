from orator import Model
from orator.orm import has_one, has_many, belongs_to, belongs_to_many

class Team(Model):

    @has_one('id')
    def plan(self):
        return Plan

class Plan(Model):

    @has_many('id')
    def releases(self):
        return Release

    @belongs_to('plan_id')
    def team(self):
        return Team

class Release(Model):

    @belongs_to('release_id')
    def plan(self):
        return Plan

    @belongs_to('id')
    def stage(self):
        return Stage

class Stage(Model):

    @has_many('release_id')
    def release(self):
        return Release
