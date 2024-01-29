import importlib
from django.core.management.base import CommandError
from django_swagger_utils.server.templates.build_app import TemplateCommand


class Command(TemplateCommand):
    help = 'My custom Django management command'

    def handle(self, **options):
        app_name = options.pop('app')
        try:
            module_name = '{}.app'.format(app_name)
            module = importlib.import_module(module_name)
            app_config = getattr(module, '{}AppConfig'.format(app_name))
        except ImportError:
            raise CommandError(
                "%r conflicts with the name of an existing Project module and "
                "cannot be used as an app name. Please try another name." % app_name
            )

        super(Command, self).handle('app', app_name, app_config=app_config, **options)