import uuid
from datetime import date as _date

from sqlalchemy import Column, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base


class Day(Base):
    __tablename__ = 'days'
    id = Column(String, primary_key=True)
    date = Column(Date)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="days")
    entries = relationship("Entry", back_populates="day")

    def __init__(self, date: _date):
        self.id = str(uuid.uuid4())
        self.date = date
