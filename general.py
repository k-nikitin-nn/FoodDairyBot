import re
from datetime import datetime


def is_date_incorrect(date: str):
    pattern = r"(?:0[1-9]|[12]\d|3[01])([.])(?:0[1-9]|1[012])\1(?:19|20)\d\d$"
    return re.match(pattern, date) is None


def is_email_incorrect(email: str):
    pattern = r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$"
    return re.match(pattern, email) is None


def is_not_number(text: str):
    return not text.isdigit()


def string_to_date(text: str, separator: str = "."):
    pattern = f"%d{separator}%m{separator}%Y"
    return datetime.strptime(text, pattern)


def string_to_int(text: str):
    return int(text)


def validation_function(fn):
    async def wrapped(**kwargs):
        message = kwargs.get("message")
        check = kwargs.get("check")
        error = kwargs.get("error")

        if check is not None and check(message.text):
            await message.answer(error)
            return False

        await fn(**kwargs)

    return wrapped


@validation_function
async def update_data(**kwargs):
    state = kwargs.get("state")
    data = kwargs.get("data")
    extra = kwargs.get("extra")
    states = kwargs.get("states")
    message = kwargs.get("message")
    next_message = kwargs.get("next_message")

    if extra is not None:
        await state.update_data({data: extra(message.text)})
    else:
        await state.update_data({data: message.text})

    if states is not None:
        await states.next()

    await message.answer(next_message)
