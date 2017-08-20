from orator import Model
from orator.orm import has_one, has_many

class Plan(Model):

    @has_many('foreign_key')
    def releases(self):
        return Release

    @belongs_to('foreign_key')
    def team(self):
        return Team
