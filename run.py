import argparse
import sys
from subprocess import run

parser = argparse.ArgumentParser()
parser.add_argument("cmd")
parser.add_argument("args", nargs=argparse.REMAINDER)
args = parser.parse_args()

if args.cmd.lower() == "test":
    command = "pytest" + ' '.join(args.args)
elif args.cmd.lower() == "run":
    command = "gunicorn -b :8000 --reload app:application --enable-stdio-inheritance"

sys.exit(run(command, shell=True).returncode)
