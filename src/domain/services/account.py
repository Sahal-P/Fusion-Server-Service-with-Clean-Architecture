from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

import hashlib
from django.http import Http404
from src.domain.services.constants import (
    JWT_ALGORITHM,
    JWT_ACCESS_EXP_DELTA_SECONDS,
    JWT_REFRESH_DAYS,
    JWT_KEY,
    JWT_REFRESH_KEY,
)
from src.domain.entities.account import TokenEntity


def create_access_token(id):
    pass
    return TokenEntity()


def decode_access_token(token):
    pass


def decode_refresh_token(token):
    pass


def create_refresh_token(id):
    pass


def generate_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def status_code_handler(exc, context):
    pass
