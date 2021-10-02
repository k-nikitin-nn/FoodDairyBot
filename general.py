import re


def is_date_incorrect(date: str):
    pattern = r"(?:0[1-9]|[12]\d|3[01])([.])(?:0[1-9]|1[012])\1(?:19|20)\d\d$"
    return re.match(pattern, date) is None


def is_email_incorrect(email: str):
    pattern = r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$"
    return re.match(pattern, email) is None
