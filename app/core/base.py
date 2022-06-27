from databases import Database
from sqlalchemy import MetaData, create_engine

from app.core.config import DB_URL

database = Database(DB_URL)
metadata = MetaData()
engine = create_engine(
    DB_URL,
)
