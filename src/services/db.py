from src.services.db_config import DATABASES
from orator import DatabaseManager, Schema

db = DatabaseManager(DATABASES)
schema = Schema(db)
