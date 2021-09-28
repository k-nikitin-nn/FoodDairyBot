from datetime import datetime

from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config import DB_NAME

engine = create_engine(f'sqlite:///{DB_NAME}]')
Base = declarative_base()
session = Session(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100))
    created_on = Column(DateTime())
    birthday = Column(DateTime())


Base.metadata.create_all(engine)


def insert_db(data: dict):
    user = User(
        id=data.get("telegram_id"),
        name=data.get("name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        created_on=datetime.now(),
        birthday=data.get("birthday")
    )
    session.add(user)


def get_user(telegram_id: int):
    return session.query(User).filter(User.id == telegram_id).all()


def init_db():
    pass
