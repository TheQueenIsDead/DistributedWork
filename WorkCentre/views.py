import pprint

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import datetime
# Create your views here.

from WorkCentre.celery import app
from celery.app.control import Inspect

def index(request):

    # pprint.pprint(app.tasks)
    # pprint.pprint(app.Task.request)

    i = app.control.inspect(['celery@DKING-LT'])

    args = {
        "time": datetime.datetime.now(),
        "tasks": {
            'active': i.active(),
            'scheduled': i.scheduled(),
            'reserved': i.reserved(),
        }
    }

    pprint.pprint(args['tasks'])

    res = render(request, "index.html", args)

    return HttpResponse(res)


from .tasks import add, wait


def create(request):
    print(f"Just received a create request! {request}")
    print("Calling the new task")
    res = wait.delay(10)
    print(f"Result: {res}")
    return HttpResponseRedirect('/work/')
