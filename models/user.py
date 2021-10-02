import uuid
from datetime import date, datetime

from sqlalchemy import Column, String, DateTime, Date, Integer
from sqlalchemy.orm import relationship
from models.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    telegram_id = Column(Integer)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    created_on = Column(DateTime)
    birthday = Column(Date)
    days = relationship("Day", back_populates="user")
    girths = relationship("Girth", back_populates="user")

    def __init__(self, name: str, last_name: str, email: str, birthday: date, telegram_id: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday
        self.telegram_id = telegram_id
        self.created_on = datetime.now()

