from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from librbac.manager import rbac


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--list-permissions', action='store_true', help='Напечатать список загруженных разрешений'
        )
        parser.add_argument(
            '--push-permissions', action='store_true', help='Сохранить загруженные разрешения в хранилище'
        )

    def _write_line(self, namespace, resource, action, scope, title):
        self.stdout.write(
            '{}\t\t{}\t\t{}\t\t{}\t\t{}\n'.format(namespace, resource, action, scope, title)
        )

    def handle(self, *args, **options):
        try:
            from librbac.config import rbac_config
        except ImportError as ie:
            raise CommandError(
                'Не удалось импортировать настройки модуля. '
                'Вероятно, система контроля доступа не сконфигурирована.'
            ) from ie

        if options['list_permissions']:
            rbac.init()
            self._write_line('namespace', 'resource', 'action', 'scope', 'title')
            for (namespace, resource, action, scope), title in rbac.permissions.items():
                self._write_line(namespace, resource, action, scope, title)
        if options['push_permissions']:
            self.stdout.write('Сохранение загруженных разрешений в хранилище...')
            rbac.init(push_permissions=True)
            self.stdout.write('Завершено.')
