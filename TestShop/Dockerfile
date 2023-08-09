FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY . /src/

RUN apt-get install -y libpq-dev

RUN pip install -r requirements.txt