import uuid
from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship
from models.database import Base


class Measurement(Base):
    __tablename__ = 'measurements'
    id = Column(String, primary_key=True)
    date = Column(DateTime)
    neck_size = Column(Integer)
    breast_size = Column(Integer)
    back_size = Column(Integer)
    stomach_size = Column(Integer)
    thigh_size = Column(Integer)
    leg_size = Column(Integer)
    hand_size = Column(Integer)
    waist_size = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User")

    def __init__(self, neck_size: int, breast_size: int, back_size: int, stomach_size: int, thigh_size: int,
                 leg_size: int, hand_size: int, waist_size: int, height: int, weight: int):
        self.id = str(uuid.uuid4())
        self.date = datetime.now()
        self.neck_size = neck_size
        self.breast_size = breast_size
        self.back_size = back_size
        self.stomach_size = stomach_size
        self.thigh_size = thigh_size
        self.leg_size = leg_size
        self.hand_size = hand_size
        self.waist_size = waist_size
        self.height = height
        self.weight = weight


