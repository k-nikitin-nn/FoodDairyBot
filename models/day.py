from sqlalchemy import Column, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base


class Day(Base):
    __tablename__ = 'days'
    id = Column(String(36), nullable=False, primary_key=True)
    date = Column(Date(), nullable=False)
    user_id = Column(String(36), ForeignKey("users.id"))
    user = relationship("User")
    entries = relationship("Entry")
