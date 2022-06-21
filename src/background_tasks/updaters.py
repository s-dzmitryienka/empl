#
import time
#
# from celery import Celery
# from core.config import CELERY_BROKER_URL
from db import users, engine
#
# celery_app = Celery('background', broker=CELERY_BROKER_URL)
# # app.config_from_object('settings', namespace='CELERY')
# celery_app.autodiscover_tasks()
#
#
# # celery -A main worker --loglevel=info
from celery import shared_task


@shared_task(bind=False, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='bg_task')
def bg_task(u_id):
    import os
    os.environ['EE_DATA_BASE_URL'] = "postgresql://root:root@localhost:32700/employment_exchange"
    os.environ['PATH'] = os.environ['PATH'] + ':/home/dzmitrock/dsa_projects/fastapi_tutor/src/'
    print(os.environ['PATH'])
    print(users)
    print('Hello BG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(f'GOT u_ID={u_id}')
    time.sleep(2)
    query = users.update().where(users.c.id == u_id).values(name='4444444444')
    engine.execute(query)
    print('FINISH BG TASK')