FROM python:3-alpine

RUN apk add --no-cache \
    gcc

COPY requirements.txt .

RUN pip install -r requirements.txt
#celery django celery[redis] redis