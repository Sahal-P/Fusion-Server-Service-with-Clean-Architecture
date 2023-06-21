from django.db import models
from typing import List
from django.utils import timezone
from django.utils.translation import gettext_lazy

from src.domain.entities.account import UserEntity


class Server(models.Model):
    name = models.CharField(gettext_lazy("name"), max_length=100)
    avatar = models.CharField(
        gettext_lazy("avatar"), max_length=100, blank=True, null=True
    )
    cover_photo = models.CharField(
        gettext_lazy("cover_photo"), max_length=100, blank=True, null=True
    )
    discription = models.TextField(
        gettext_lazy("discription"), db_index=True, blank=True, null=True
    )
    accessibility = models.CharField(gettext_lazy("accessibility"), max_length=15)
    owner = models.CharField(gettext_lazy("owner"), max_length=64)
    is_active = models.BooleanField(gettext_lazy("active"), default=True)

    class Meta:
        verbose_name = gettext_lazy("name")
        verbose_name_plural = gettext_lazy("name")
        ordering = ("name",)

    def __str__(self) -> str:
        return str(self.map())

    def map(self, fields: List[str] = None) -> UserEntity:
        fields = fields or [str(field) for field in UserEntity.__dataclass_fields__]
        attrs = {field: getattr(self, field) for field in fields}
        return UserEntity(**attrs)


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    expired_at = models.DateTimeField()
