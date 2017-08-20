from orator import Model
from orator.orm import has_one, belongs_to

class Release(Model):

    @has_one('foreign_key')
    def project(self):
        return Project

    @belongs_to('foreign_key')
    def plan(self):
        return Plan
