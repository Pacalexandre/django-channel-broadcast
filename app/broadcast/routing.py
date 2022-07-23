from django.urls import path

from .consumers import JokerConsumer


ws_urlpatterns = [
    path('ws/broadcast/', JokerConsumer.as_asgi()),
]