# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task, task


@shared_task
def add(x, y):
    return x + y


# @shared_task
# def wait(x):
#     time.sleep(x)
#     return None

@task
def wait(seconds):
    # total_work_to_do = len(list_of_work)
    for second in range(seconds):
        print(f"Waiting on the {second} second")
        time.sleep(1)
    return 'work is complete'



