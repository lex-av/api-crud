from src.db.base import database
from src.repositories.repo_user import UserRepository


def get_user_repo() -> UserRepository:
    return UserRepository(database)
