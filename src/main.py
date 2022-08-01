import uvicorn
import aioredis
from celery import Celery
from fastapi import FastAPI

from core.config import CELERY_BROKER_URL, REDIS_URL
from db.base import database
from endpoints.users import router

from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from admin.models import Admin


app = FastAPI(title='EE')
app.include_router(router=router, prefix='/users', tags=['users'])

celery_app = Celery('background', broker=CELERY_BROKER_URL)
celery_app.autodiscover_tasks()


@app.on_event("startup")
async def startup():
    await database.connect()

    redis = await aioredis.create_redis_pool(address=REDIS_URL)
    await admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        template_folders=["templates"],
        providers=[
            UsernamePasswordProvider(
                login_logo_url="https://preview.tabler.io/static/logo.svg", admin_model=Admin
            )
        ],
        redis=redis,
    )


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0')
