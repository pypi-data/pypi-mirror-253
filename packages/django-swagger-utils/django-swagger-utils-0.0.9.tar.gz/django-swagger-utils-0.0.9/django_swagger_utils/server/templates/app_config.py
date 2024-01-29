APP_CONFIG = """
from django.apps import AppConfig


class {{app}}AppConfig(AppConfig):
    name = "{{app}}"

    def ready(self):
        from {{app}} import signals # pylint: disable=unused-variable
"""
