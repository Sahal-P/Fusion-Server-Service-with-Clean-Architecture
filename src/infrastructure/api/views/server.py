from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from src.infrastructure.orm.db.handle_server.admin import produce_messages

from src.interface.controllers.account import ServerController


class ServerViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> ServerController:
        return self.viewset_factory.create()

    def create_server(self, request: Request, *args, **kwargs) -> Response:
        data = request.data
        payload, status = self.controller.create_server(data)
        return Response(data=payload, status=status)
