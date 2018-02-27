from os import path

import yaml

filepath = path.abspath(path.dirname(__file__))
path = path.join(filepath, "../../config.yaml")

with open(path, 'r') as f:
    Config = yaml.load(f)

