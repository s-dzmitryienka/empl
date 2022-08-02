import sqlalchemy
import datetime
from sqlalchemy.orm import registry


from db.base import metadata

mapper_registry = registry()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('email', sqlalchemy.String, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('hashed_password', sqlalchemy.String),
    sqlalchemy.Column('is_company', sqlalchemy.Boolean),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)

class User:
    id: str
    email: str

    @property
    def id_email(self):
        value = f'{self.id}-{self.email}'
        print('!!**!!'* 100, value)
        return value

mapper_registry.map_imperatively(User, users)
