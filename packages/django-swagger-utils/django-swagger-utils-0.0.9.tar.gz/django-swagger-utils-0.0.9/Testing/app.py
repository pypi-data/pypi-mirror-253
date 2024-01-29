
from django.apps import AppConfig


class TestingAppConfig(AppConfig):
    name = "Testing"

    def ready(self):
        from Testing import signals # pylint: disable=unused-variable
