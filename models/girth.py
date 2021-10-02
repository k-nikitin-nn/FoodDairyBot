import uuid
from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime, Integer, Float
from sqlalchemy.orm import relationship
from models.database import Base


class Girth(Base):
    __tablename__ = 'girths'
    id = Column(String, primary_key=True)
    date = Column(DateTime)
    neck = Column(Integer)
    breast = Column(Integer)
    back = Column(Integer)
    belly = Column(Integer)
    thigh = Column(Integer)
    leg = Column(Integer)
    hand = Column(Integer)
    waist = Column(Integer)
    height = Column(Integer)
    weight = Column(Float)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="girths")

    def __init__(self, neck: int, breast: int, back: int, belly: int, thigh: int,
                 leg: int, hand: int, waist: int, height: int, weight: int):
        self.id = str(uuid.uuid4())
        self.date = datetime.now()
        self.neck = neck
        self.breast = breast
        self.back = back
        self.belly = belly
        self.thigh = thigh
        self.leg = leg
        self.hand = hand
        self.waist = waist
        self.height = height
        self.weight = weight


