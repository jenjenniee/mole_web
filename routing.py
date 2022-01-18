from django.urls import path
from . import consumers

websocket_urlpatterns = [
    
    path('ws/moleGame/', consumers.MoleGameConsumer.as_asgi()), 

]