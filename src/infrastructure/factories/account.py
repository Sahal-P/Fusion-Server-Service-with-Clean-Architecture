from src.infrastructure.orm.db.handle_server.repositories import (
    ServerDataBaseRepository,
)
from src.interface.controllers.account import ServerController
from src.interface.repositories.account import ServerRepository
from src.usecase.account import ServerInteractor


class ServerDataBaseRepositoryFactory:
    @staticmethod
    def get() -> ServerDataBaseRepository:
        return ServerDataBaseRepository()


class ServerRepositoryFactory:
    @staticmethod
    def get() -> ServerRepository:
        db_repo = ServerDataBaseRepositoryFactory.get()
        return ServerRepository(db_repo)


class ServerInteractorFactory:
    @staticmethod
    def get() -> ServerInteractor:
        user_repo = ServerRepositoryFactory.get()
        return ServerInteractor(user_repo)


class ServerViewSetFactory:
    @staticmethod
    def create() -> ServerController:
        user_interactor = ServerInteractorFactory.get()
        return ServerController(user_interactor)
