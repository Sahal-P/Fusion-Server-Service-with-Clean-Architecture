from django.apps import AppConfig


class ServerConfig(AppConfig):
    label = 'server'
    name = 'src.infrastructure.orm.db.server'
    verbose_name = 'Server'
