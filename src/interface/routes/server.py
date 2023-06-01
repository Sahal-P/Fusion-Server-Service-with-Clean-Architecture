from src.interface.controllers.account import ServerController
from src.interface.routes.core.constants import HTTP_VERB_GET, HTTP_VERB_POST
from src.interface.routes.core.routing import Route, Router

server_router = Router()
server_router.register([
    Route(
        http_verb=HTTP_VERB_GET,
        path=r'^create/$',
        controller= ServerController,
        method='create_server',
        name='create_server',
    ),
])