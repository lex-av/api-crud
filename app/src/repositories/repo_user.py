import datetime
from typing import List, Optional

from src.core.security import hash_password
from src.db.user import user
from src.models.model_user import User, UserInput

from .repo_base import BaseRepository


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = user.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, search_id: int) -> Optional[User]:
        query = user.select().where(user.c.id == search_id)
        current_user = await self.database.fetch_one(query)
        if current_user is None:
            return None
        return User.parse_obj(current_user)

    async def get_by_email(self, email: str) -> Optional[User]:
        query = user.select().where(user.c.email == email)
        current_user = await self.database.fetch_one(query)
        if current_user is None:
            return None
        return User.parse_obj(current_user)

    async def create(self, user_in: UserInput) -> User:
        new_user = User(
            name=user_in.name,
            email=user_in.email,
            hashed_password=hash_password(user_in.password),
            is_company=user_in.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**new_user.dict()}
        values.pop("id", None)
        query = user.insert().values(**values)
        new_user.id = await self.database.execute(query)
        return new_user

    async def update(self, id_upd: int, user_in: UserInput) -> User:
        upd_user = User(
            id=id_upd,
            name=user_in.name,
            email=user_in.email,
            hashed_password=hash_password(user_in.password_confirm),
            is_company=user_in.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**upd_user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = user.update().where(user.c.id == id_upd).values(**values)
        upd_user.id = await self.database.execute(query)
        return upd_user
