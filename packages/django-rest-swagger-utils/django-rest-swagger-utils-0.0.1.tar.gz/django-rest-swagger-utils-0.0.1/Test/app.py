
from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = "Test"

    def ready(self):
        from Test import signals # pylint: disable=unused-variable
