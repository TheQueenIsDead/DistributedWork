from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import datetime
# Create your views here.


def index(request):

    args = {
        "time": datetime.datetime.now()
    }
    res = render(request, "index.html", args)
    return HttpResponse(res)


from .tasks import add, wait
def create(request):
    print(f"Just received a create request! {request}")
    print("Calling the new task")
    res = wait(10)
    print(f"Result: {res}")
    return HttpResponseRedirect('/work/')