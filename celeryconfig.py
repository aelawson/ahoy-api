from src.services.config import Config

broker_url = 'redis://{host}:{port}/{database}'.format(
    host=Config['broker']['host'],
    port=Config['broker']['port'],
    database=Config['broker']['database']
)
result_backend = 'redis://{host}:{port}/{database}'.format(
    host=Config['backend']['host'],
    port=Config['backend']['port'],
    database=Config['backend']['database']
)
result_expires = None
accept_content = ['application/json']
include = [
    'src.tasks.release',
    'src.tasks.cut'
]
enable_utc = True

task_serializer = 'json'
task_reject_on_worker_lost = True
task_acks_late = True

