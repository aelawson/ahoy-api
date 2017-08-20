from orator import Model
from orator.orm import belongs_to

class Stage(Model):

    @belongs_to('foreign_key')
    def release_stage(self):
        return ReleaseStage
