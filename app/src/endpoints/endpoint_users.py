from typing import List

from fastapi import APIRouter, Depends
from src.models.model_user import User, UserInput, UserOut
from src.repositories.repo_user import UserRepository

from .depends import get_user_repo

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repo), limit: int = 100, skip: int = 1):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/create", response_model=UserOut)
async def create_user(user: UserInput, users: UserRepository = Depends(get_user_repo)):
    return await users.create(user_in=user)


@router.put("/update", response_model=UserOut)
async def update_user(id: int, user: UserInput, users: UserRepository = Depends(get_user_repo)):
    return await users.update(id_upd=id, user_in=user)
