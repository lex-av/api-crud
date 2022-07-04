from fastapi import APIRouter, Depends, HTTPException, status
from src.core.security import create_access_token, verify_password
from src.models.model_token import Login, Token
from src.repositories.repo_user import UserRepository

from .depends import get_user_repo

router = APIRouter()


@router.post("/", response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repo)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect user credentials")
    return Token(access_string=create_access_token({"sub": user.email}), token_type="Bearer")
