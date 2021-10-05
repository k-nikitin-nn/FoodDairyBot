import uuid

from sqlalchemy import Column, String, ForeignKey, Date, Integer, Float
from sqlalchemy.orm import relationship
from models.database import Base


class Girth(Base):
    __tablename__ = 'girths'
    id = Column(String, primary_key=True)
    date = Column(Date)
    neck = Column(Integer)
    breast = Column(Integer)
    back = Column(Integer)
    waist = Column(Integer)
    belly = Column(Integer)
    thigh = Column(Integer)
    hand = Column(Integer)
    foot = Column(Integer)
    weight = Column(Float)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="girths")

    def __init__(self, date: date, neck: int, breast: int, back: int, belly: int, thigh: int,
                 foot: int, hand: int, waist: int, weight: int, user_id: str):
        self.id = str(uuid.uuid4())
        self.date = date
        self.neck = neck
        self.breast = breast
        self.back = back
        self.belly = belly
        self.thigh = thigh
        self.foot = foot
        self.hand = hand
        self.waist = waist
        self.weight = weight
        self.user_id = user_id


