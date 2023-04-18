
from django.urls import path, include
from . import consumers

websocket_urlpatterns = [
    path('ws/books/', consumers.BooksConsumer.as_asgi()),
]