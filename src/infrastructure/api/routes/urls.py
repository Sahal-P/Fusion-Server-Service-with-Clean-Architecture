# coding: utf-8

from django.conf import settings
from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path('', include(f'{settings.API_ROUTES}.server.urls')),
]
# handler404 = 'src.infrastructure.api.views.account.NotFoundAPIException'
