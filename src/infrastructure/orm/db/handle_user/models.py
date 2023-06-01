from django.db import models
from typing import List
from django.utils import timezone
from django.utils.translation import gettext_lazy

from src.domain.entities.account import UserEntity

class User(models.Model):
    user_id = models.IntegerField(gettext_lazy('user_id'))
    name = models.CharField(gettext_lazy('name'), max_length=100, blank=True)
    surname = models.CharField(gettext_lazy('surname'), max_length=100, blank=True, null=True)
    username = models.CharField(gettext_lazy('username'), max_length=20, blank=True)
    email = models.EmailField(gettext_lazy('email'), db_index=True, unique=True)
    phone = models.CharField(gettext_lazy('phone'),max_length=15, unique=True)
    is_active = models.BooleanField(gettext_lazy('active'), default=True)
    
    class Meta:
        verbose_name = gettext_lazy('handle_user')
        verbose_name_plural = gettext_lazy('handle_user')
        ordering = ('email',)
        
    def __str__(self) -> str:
        return str(self.map())
        
    def map(self, fields: List[str] = None) -> UserEntity:
        fields = fields or [str(field) for field in UserEntity.__dataclass_fields__]
        attrs = {field: getattr(self, field) for field in fields}
        return UserEntity(**attrs)