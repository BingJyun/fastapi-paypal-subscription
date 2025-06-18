from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

DB_URL = settings.DB_URL
engine = create_engine(DB_URL, echo=True)

class Base(DeclarativeBase):
    pass