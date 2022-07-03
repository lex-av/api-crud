from fastapi import APIRouter, Depends
from src.repositories.repo_user import UserRepository

from .depends import get_user_repo

router = APIRouter()


@router.get("/")
async def read_users(users: UserRepository = Depends(get_user_repo), limit: int = 100, skip: int = 1):
    return {}
