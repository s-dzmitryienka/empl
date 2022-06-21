import os

from starlette.config import Config

config = Config('.env')

DATABASE_URL = config('EE_DATA_BASE_URL', cast=str, default='')


# Celery config
CELERY_RABBIT_HOST = os.getenv('CELERY_RABBIT_HOST', 'localhost')
CELERY_RABBIT_PORT = os.getenv('CELERY_RABBIT_PORT', '5672')
CELERY_RABBIT_USER = os.getenv('CELERY_RABBIT_USER', 'guest')
CELERY_RABBIT_PASSWORD = os.getenv('CELERY_RABBIT_PASSWORD', 'guest')
CELERY_MESSAGE_BROKER = os.getenv('CELERY_MESSAGE_BROKER', 'amqp')

CELERY_BROKER_URL = f'{CELERY_MESSAGE_BROKER}://{CELERY_RABBIT_USER}:{CELERY_RABBIT_PASSWORD}@{CELERY_RABBIT_HOST}:{CELERY_RABBIT_PORT}'