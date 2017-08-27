from orator import Model
from orator.orm import has_one, has_many, belongs_to

class Team(Model):

    @has_one('foreign_key')
    def plan(self):
        return Plan

class Plan(Model):

    @has_many('foreign_key')
    def releases(self):
        return Release

    @belongs_to('foreign_key')
    def team(self):
        return Team

class Release(Model):

    @has_one('foreign_key')
    def project(self):
        return Project

    @has_one('foreign_key')
    def project(self):
        return Stage

    @belongs_to('foreign_key')
    def plan(self):
        return Plan

class Stage(Model):

    @belongs_to('foreign_key')
    def release(self):
        return Release
