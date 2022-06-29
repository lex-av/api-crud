from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str = "default"

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
DB_URL = settings.db_url
