from orator import Model
from orator.orm import belongs_to

class Project(Model):

    @belongs_to('foreign_key')
    def team(self):
        return Team
