from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from librbac.contrib.migrations.loader.disk import MigrationLoader
from librbac.contrib.migrations.orchestrator import MigrationOrchestrator
from librbac.contrib.migrations.recorder.local_db import MigrationRecorder
from librbac.manager import rbac


class Command(BaseCommand):

    help = 'Выполнить миграцию разрешений'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help=(
                'Пробный запуск миграций. Выполняется только сборка и проверка целостности. '
                'Обработка событий не выполняется.'
            )
        )

    def handle(self, *args, **options):
        try:
            from librbac.config import rbac_config
        except ImportError as ie:
            raise CommandError(
                'Не удалось импортировать настройки модуля. '
                'Вероятно, система контроля доступа не сконфигурирована.'
            ) from ie

        rbac.init()
        orchestrator = MigrationOrchestrator(loader=MigrationLoader, recorder=MigrationRecorder)
        orchestrator.apply_migrations(dry_run=options['dry_run'])
