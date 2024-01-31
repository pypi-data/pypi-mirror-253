
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = "Users"

    def ready(self):
        from Users import signals # pylint: disable=unused-variable
