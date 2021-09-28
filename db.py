from models.database import create_db, Session
from  models.day import Day
from  models.user import User
from  models.measurement import Measurement
from  models.entry import Entry


def create(load_fake_data: bool = False):
    create_db()

    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    ...

