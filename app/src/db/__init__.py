from .base import engine, metadata
from .job import job
from .user import user

# Create database tables on import
metadata.create_all(bind=engine)
