import uvicorn
from celery import Celery
from fastapi import FastAPI

from core.config import CELERY_BROKER_URL
from db.base import database
from endpoints.users import router

app = FastAPI(title='EE')
app.include_router(router=router, prefix='/users', tags=['users'])

celery_app = Celery('background', broker=CELERY_BROKER_URL)
celery_app.autodiscover_tasks()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0')
