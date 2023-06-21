from rest_framework.routers import Route, SimpleRouter

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from src.infrastructure.factories.account import ServerViewSetFactory
from src.interface.routes.server import server_router


class ServerRouter(SimpleRouter):
    routes = [
        Route(
            url=server_router.get_url("create_server"),
            mapping=server_router.map("create_server"),
            initkwargs={"viewset_factory": ServerViewSetFactory},
            name="{basename}-create",
            detail=False,
        )
    ]
