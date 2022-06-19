from datetime import datetime
from typing import List, Optional

from core.security import hash_password
from db import users
from models.users import User, UserIn
from repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, _id: int) -> Optional[User]:
        query = users.select().where(users.c.id == _id)
        user = await self.database.fetch_one(query)
        if user is None:
            return
        return User.parse_obj(user)

    async def get_by_email(self, email: str) -> Optional[User]:
        query = users.select().where(users.c.email == email).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        values = user.dict()
        values.pop('id', None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, _id: int, u: UserIn) -> User:
        user = User(
            id=_id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            updated_at=datetime.utcnow(),
        )
        values = user.dict()
        values.pop('id', None)
        values.pop('created_at', None)
        query = users.update().where(users.c.id == _id).values(**values)
        await self.database.execute(query)
        return user

    async def delete(self, user_id: int) -> None:
        pass
