import uvicorn
from celery import Celery
from fastapi import FastAPI
from core import config
from core.config import CELERY_BROKER_URL
from db.base import database
from endpoints.users import router
from sqladmin import Admin, ModelView
from db.base import engine
from db.users import User


app = FastAPI(title='EE')
app.include_router(router=router, prefix='/users', tags=['users'])

celery_app = Celery('background', broker=CELERY_BROKER_URL)
celery_app.autodiscover_tasks()

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.email]
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"
    column_searchable_list = [User.name]

admin.add_view(UserAdmin)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0')
