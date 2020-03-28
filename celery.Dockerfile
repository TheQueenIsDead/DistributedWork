FROM python:3-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt
#celery django celery[redis] redis