import uuid
from datetime import date, datetime

from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.orm import relationship
from models.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100))
    created_on = Column(DateTime())
    birthday = Column(Date())
    days = relationship("Day")

    def __init__(self, name: str, last_name: str, email: str, birtday: date):
        self.id = str(uuid.uuid4())
        self.name = name
        self.last_name = last_name
        self.email = email
        self.birthday = birtday
        self.created_on = datetime.now()

