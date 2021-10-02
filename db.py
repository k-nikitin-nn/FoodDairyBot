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
