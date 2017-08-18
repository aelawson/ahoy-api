
import os

from orator import DatabaseManager

db_config = {
    'postgres': {
        'driver': 'postgres',
        'host': os.environ.get('DB_HOST', 'localhost'),
        'database': os.environ.get('DB_DATABASE', 'database'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASS', 'root'),
        'prefix': os.environ.get('DB_PREFIX', '')
    }
}

db = DatabaseManager(db_config)
