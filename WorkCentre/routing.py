from channels.routing import ProtocolTypeRouter, URLRouter
from .urls import websocket_urlpatterns
application = ProtocolTypeRouter({
    # (http->Django views is added by default)
    'websocket':
        URLRouter(
            websocket_urlpatterns
        ),
})