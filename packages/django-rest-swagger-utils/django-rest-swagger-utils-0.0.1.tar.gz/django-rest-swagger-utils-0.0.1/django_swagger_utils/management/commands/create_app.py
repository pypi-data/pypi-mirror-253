from importlib import import_module
from django.core.management.base import CommandError
from django_swagger_utils.server.templates.app_template import TemplateCommand


class Command(TemplateCommand):
    help = 'My custom Django management command'

    def handle(self, **options):
        app_name = options.pop('app')

        try:
            import_module(app_name)
        except ImportError:
            pass
        else:
            raise CommandError(
                "%r conflicts with the name of an existing Project module and "
                "cannot be used as an app name. Please try another name." % app_name
            )

        super(Command, self).handle('app', app_name, **options)