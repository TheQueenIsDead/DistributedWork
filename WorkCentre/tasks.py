# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def wait(x):
    time.sleep(x)
    return None


@shared_task
def xsum(numbers):
    return sum(numbers)

