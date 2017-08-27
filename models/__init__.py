from orator import Model
from src.services.db import db

Model.set_connection_resolver(db)
