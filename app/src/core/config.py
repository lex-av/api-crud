from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = "default"
    secret_key: str = "unsecure_default_029384636342"

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
DB_URL = settings.db_url

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ENCODE_ALOGITHM = "HS256"
SECRET_KEY = settings.secret_key
