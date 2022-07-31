import os

from starlette.config import Config

config = Config('.env')

# DATABASE_URL = config('EE_DATA_BASE_URL', cast=str, default='')
DB = 'postgresql'
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

DATABASE_URL = f"{DB}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# msg broker conf
RABBIT_HOST = os.getenv('RABBIT_HOST', 'localhost')
RABBIT_PORT = os.getenv('RABBIT_PORT', '5672')
RABBIT_USER = os.getenv('RABBIT_USER', 'guest')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD', 'guest')

# celery conf
MESSAGE_BROKER = os.getenv('MESSAGE_BROKER', 'amqp')
CELERY_BROKER_URL = f'{MESSAGE_BROKER}://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_HOST}:{RABBIT_PORT}'
