from django.urls import path
from operators.consumers OrderConsumer


websocket_urlpatterns=[
    path("ws/orders/", OrderConsumer.as_asgi())
]