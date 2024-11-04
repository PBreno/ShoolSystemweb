
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker,declarative_base

from .settings import settings

SQLALCHEMY_DATABASE_URL = (f'postgresql://{settings.database_username}:'
                           f'{settings.database_password}@'
                           f'{settings.database_host}:{settings.database_port}/'
                           f'{settings.database_name}')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    print('bd')
    try:
        yield db
    finally:
        db.close()

