FROM python:3.8

WORKDIR /FooddairyBot

ENV VIRTUAL_ENV=/FooddairyBot/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -U pip install -r requirements.txt

COPY . .
CMD ["python", "bot.py"]