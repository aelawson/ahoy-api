from orator import Model
from orator.orm import has_one, belongs_to

class ReleaseStage(Model):

    @has_one('foreign_key')
    def stage(self):
        return Stage

    @belongs_to('foreign_key')
    def release(self):
        return Release
