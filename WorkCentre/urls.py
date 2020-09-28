from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
]
#
# websocket_urlpatterns = [
#     url(r'^ws/chat/$', consumers.ChatConsumer),
# ]