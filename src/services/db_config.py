import os

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': os.environ.get('DB_HOST', 'localhost'),
        'port': os.environ.get('DB_PORT', '5432'),
        'database': os.environ.get('DB_DATABASE', 'database'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASS', 'root'),
        'prefix': os.environ.get('DB_PREFIX', '')
    }
}
