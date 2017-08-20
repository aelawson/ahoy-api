from orator import Model
from orator.orm import has_many

class Team(Model):

    @has_many('foreign_key')
    def projects(self):
        return Project

    @has_many('foreign_key')
    def releases(self):
        return Release
