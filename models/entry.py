import enum
import uuid
from datetime import time as _time

from sqlalchemy import Column, String, ForeignKey, Time, Enum
from sqlalchemy.orm import relationship
from models.database import Base


class MealTime(enum.Enum):
    breakfast = "Завтрак",
    lunch = "Обед",
    dinner = "Ужин",
    snacking = "Перекус",
    water = "Вода"


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(String, primary_key=True)
    time = Column(Time)
    mealtime = Column(Enum(MealTime))
    text = Column(String)
    day_id = Column(String, ForeignKey("days.id"))
    day = relationship("Day", back_populates="entries")

    def __init__(self, time: _time, mealtime: str, text: str):
        self.id = str(uuid.uuid4())
        self.time = time
        self.mealtime = mealtime
        self.text = text
