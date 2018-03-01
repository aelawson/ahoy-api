from celery_app import celery_app
from models.models import Release, Stage
from src.services.release import ReleaseService

@celery_app.task()
def release(task_metadata={}):
    release_id = task_metadata.get('release_id')

    release = Release.find(release_id)

    ReleaseService.release(release)

    next_stage = Stage.where('name', '=', 'Production').first()

    release.stage_id = next_stage.id
    release.save()

    return release.serialize()

