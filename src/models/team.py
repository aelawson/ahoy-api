from orator import Model
from orator.orm import has_many

class Team(Model):

    @has_many('foreign_key')
    def projects(self):
        return Project

    @has_one('foreign_key')
    def plan(self):
        return Plan
