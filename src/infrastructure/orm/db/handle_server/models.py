from django.db import models
from typing import List
from django.utils import timezone
from django.utils.translation import gettext_lazy

from src.domain.entities.account import UserEntity
from src.infrastructure.orm.db.handle_user.models import User


class Server(models.Model):
    name = models.CharField(gettext_lazy("name"), max_length=100)
    avatar = models.ImageField(gettext_lazy("avatar"), upload_to="Server_avatar")
    cover_photo = models.CharField(
        gettext_lazy("cover_photo"), max_length=100, blank=True, null=True
    )
    discription = models.TextField(
        gettext_lazy("discription"), db_index=True, blank=True, null=True
    )
    accessibility = models.CharField(gettext_lazy("accessibility"), max_length=15)
    owner = models.CharField(gettext_lazy("owner"), max_length=64)
    is_active = models.BooleanField(gettext_lazy("active"), default=True)
    members = models.ManyToManyField(User, related_name="servers")

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


class Channel(models.Model):
    CHANNEL_TYPES = (
        ("audio", "Audio"),
        ("text", "Text"),
        ("video", "Video"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    type_of = models.CharField(max_length=10, choices=CHANNEL_TYPES)
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="channels"
    )

    def __str__(self):
        return f"{self.server.name} - {self.name}"


class Messages(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_message"
    )
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="messages"
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    replay_to = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="replies"
    )
    reactions = models.ManyToManyField(
        User, through="Reaction", related_name="reactions"
    )

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.sender.username} -> {self.channel.server.name} -> {self.channel.name}: {self.message}"


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Messages, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} reacted {self.emoji} to {self.message}"
