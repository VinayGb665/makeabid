from alembic import context, config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from configparser import ConfigParser
 
from functools import lru_cache
from typing import Generator
import os

config = ConfigParser()
config.read("alembic.ini")

url = os.environ.get("DATABASE_URL", "postgresql://localhost:5432/makeabid")
engine = create_engine(url, pool_pre_ping=True)

@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return Session

def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()