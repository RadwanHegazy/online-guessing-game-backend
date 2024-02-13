from .consumers import SearchBattleConsumer
from django.urls import path

websocket_urlpatterns = [
    path('search-battle/',SearchBattleConsumer.as_asgi())
]