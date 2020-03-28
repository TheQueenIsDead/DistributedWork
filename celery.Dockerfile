FROM python:3-alpine

RUN pip install celery django celery[redis] redis