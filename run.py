import argparse
import sys
from subprocess import run

parser = argparse.ArgumentParser()
parser.add_argument("cmd")
parser.add_argument("args", nargs=argparse.REMAINDER)
args = parser.parse_args()

if args.cmd.lower() == "test":
    command = "pytest" + ' '.join(args.args)
elif args.cmd.lower() == 'migrate':
    command = 'orator migrate -c ./src/services/db_config.py'
elif args.cmd.lower() == 'migrations':
    command = 'orator migrate:status -c ./src/services/db_config.py'
elif args.cmd.lower() == 'refresh':
    command = 'orator migrate:refresh -c ./src/services/db_config.py --seed'
elif args.cmd.lower() == 'rollback':
    command = 'orator migrate:reset  -c ./src/services/db_config.py'
elif args.cmd.lower() == "run":
    command = "gunicorn -b :8000 --reload app:application --enable-stdio-inheritance"

sys.exit(run(command, shell=True).returncode)
