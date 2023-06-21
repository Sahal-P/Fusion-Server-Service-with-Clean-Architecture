import logging
from http import HTTPStatus
from typing import Tuple

# from src.domain.exceptions import EntityDuplicate
from rest_framework import exceptions

# from src.domain.services.account import create_access_token, create_refresh_token
from src.interface.serializers.account import (
    UserRegisterSerializer,
    NewUserSerializer,
    UserLoginSerializer,
    TokenSerializer,
    RefreshTokenSerializer,
    UserSerializer,
)
from src.interface.middlewares.auth import Jwt_auth_required
from colorama import Fore

logger = logging.getLogger(__name__)


class ServerController:
    def __init__(self, user_interactor):
        self.user_interactor = user_interactor

    def create_server(self, params: dict) -> Tuple[dict, int]:
        return None, HTTPStatus.OK.value
