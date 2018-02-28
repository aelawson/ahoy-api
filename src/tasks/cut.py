from celery_app import celery_app
from models.models import Release, Stage
from src.services.release import ReleaseService

@celery_app.task()
def cut(task_metadata={}):
    release_id = task_metadata.get('release_id')
    tag = task_metadata.get('tag')

    release = Release.find(release_id)

    ReleaseService.cut(release, tag)

    next_stage = Stage.where('name', '=', 'Staging').first()

    release.stage_id = next_stage.id
    release.save()

    return release.serialize()

