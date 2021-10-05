from sqlalchemy import desc

from models.database import create_db, Session
from models.day import Day
from models.user import User
from models.girth import Girth
from models.entry import Entry

session = Session()


def create(load_fake_data: bool = False):
    create_db()

    if load_fake_data:
        _load_fake_data()


def _load_fake_data():
    ...


def session_commit(data):
    session.add(data)
    session.commit()


def create_user(data: dict):
    telegram_id = data.get("telegram_id")
    name = data.get("name")
    last_name = data.get("last_name")
    email = data.get("email")
    birthday = data.get("birthday")

    user = User(name, last_name, email, birthday, telegram_id)
    session_commit(user)


def get_user(telegram_id: int):
    return session.query(User).filter(User.telegram_id == telegram_id).all()


def create_girth(data: dict):
    date = data.get("date")
    neck = data.get("neck")
    breast = data.get("breast")
    back = data.get("back")
    belly = data.get("belly")
    thigh = data.get("thigh")
    foot = data.get("foot")
    hand = data.get("hand")
    waist = data.get("waist")
    height = data.get("height")
    weight = data.get("weight")
    user_id = data.get("user_id")

    girth = Girth(date, neck, breast, back, belly, thigh, foot, hand, waist, height, weight, user_id)
    session_commit(girth)


def get_girths(telegram_id: int):
    return session.query(Girth) \
        .order_by(Girth.date) \
        .join(User) \
        .filter(User.telegram_id == telegram_id) \
        .all()
