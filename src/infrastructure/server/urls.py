from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/server/",
        include((f"{settings.API_ROUTES}.urls", "api"), namespace="api"),
    ),
]
