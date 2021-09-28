import enum

from sqlalchemy import Column, String, ForeignKey, Time, Enum
from sqlalchemy.orm import relationship
from models.database import Base


class MealTime(enum.Enum):
    breakfast = "Завтрак",
    lunch = "Ланч",
    dinner = "Ужин",
    snacking = "Перекус",
    water = "Вода"


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(String(36), nullable=False, primary_key=True)
    time = Column(Time())
    mealtime = Column(Enum(MealTime))
    text = Column(String(), nullable=False)
    day_id = Column(String(36), ForeignKey("days.id"))
    day = relationship("Day")
