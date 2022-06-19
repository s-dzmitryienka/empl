from typing import List

from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository
from models.users import User, UserIn
from repositories.users import UserRepository

router = APIRouter()


@router.get(path='/', response_model=List[User])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0,
):
    return await users.get_all(limit=limit, skip=skip)


@router.post(path='/', response_model=User)
async def read_users(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
):
    return await users.create(user)


@router.get(path='/{user_id}', response_model=User)
async def get_user_by_id(
        user_id: int,
        users: UserRepository = Depends(get_user_repository),
):
    return await users.get_by_id(user_id)
