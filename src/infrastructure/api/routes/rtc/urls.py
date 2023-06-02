# coding: utf-8

from django.conf.urls import include
from django.urls import path
from django.urls import re_path
from src.infrastructure.api.views.rtc import consumer

websocket_urlpatterns = [
    re_path(r'ws/socket/(?P<room_name>\w+)/$', consumer.SignalConsumer.as_asgi()),
    re_path(r'ws/socket/user/(?P<room_name>\w+)/$', consumer.UserConnection.as_asgi())
]

# print(user_router.registry)
