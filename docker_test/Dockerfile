FROM python:3.10

WORKDIR /app

COPY requirements.txt .

ENV build_from=docker

RUN pip install -r requirements.txt

COPY . .
