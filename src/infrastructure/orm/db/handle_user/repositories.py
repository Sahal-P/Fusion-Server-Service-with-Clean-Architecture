from django.db.utils import IntegrityError
from django.utils import timezone
import datetime
from src.domain.entities.account import UserEntity, TokenEntity
from .models import User
from rest_framework import exceptions
from src.domain.exceptions import EntityDuplicate, EntityDoesNotExist, InvalidToken


class UserDataBaseRepository:
    def create_user(
        self,
        email: str,
        phone: str,
        username: str,
        name: str,
        id: int,
        surname: str = None,
    ) -> UserEntity:
        try:
            user = User.objects.create(
                email=email,
                user_id=id,
                phone=phone,
                username=username,
                name=name,
                surname=surname,
            )
            return user
        except IntegrityError:
            pass

    def get(self, email: str, password: str) -> UserEntity:
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            raise EntityDoesNotExist(message="User does not exits with this data")
            # raise exceptions.NotAuthenticated('User does not exits with this data')
        return user.map(fields=["id", "username", "email", "is_active", "last_login"])
