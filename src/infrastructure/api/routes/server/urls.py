# coding: utf-8

from django.conf.urls import include
from django.urls import path
from django.urls import re_path


from src.infrastructure.api.routes.server.routers import ServerRouter
from src.infrastructure.api.views.server import ServerViewSet

server_router = ServerRouter()
server_router.register('', viewset=ServerViewSet, basename='server')

urlpatterns = [
    path('', include(server_router.urls)),
]

# print(user_router.registry)
