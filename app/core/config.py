from starlette.config import Config

config = Config(".env")

DB_URL = config("APP_DB_URL", cast=str, default="")
