from importlib import import_module
from itertools import chain
from itertools import product
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING
from typing import Generator
from typing import Tuple

from django.apps import apps
from pydantic.tools import parse_file_as

from ..types import Migration
from ..types import MigrationLoaderInterface


if TYPE_CHECKING:
    from django.apps.config import AppConfig


class MigrationLoader(MigrationLoaderInterface):

    """Загрузчик миграций с диска"""

    _disk_migrations: dict[tuple[str, str], Migration]

    def __init__(self):
        self._disk_migrations = {}

        self._load_disk()

    @classmethod
    def _get_app_permissions_modules(cls) -> Generator[Tuple[ModuleType, 'AppConfig'], None, None]:
        """Возвращает модули permissions из приложений системы."""
        for app_config in apps.get_app_configs():
            try:
                yield import_module('.permissions', app_config.name), app_config
            except ImportError as error:
                if 'No module named' not in error.args[0]:
                    raise
                continue

    def _load_disk(self):
        """Load the migrations from all INSTALLED_APPS from disk."""

        for permission_module, app_config in self._get_app_permissions_modules():
            migrations_dir_path = Path(permission_module.__file__).parent / 'migrations'
            if not migrations_dir_path.is_dir():
                continue

            for migration_file_path in sorted(migrations_dir_path.iterdir(), key=lambda fn: fn.name):
                # Check if the file name starts with a number
                if not (migration_file_path.name[:4].isdigit() and migration_file_path.is_file()):
                    raise ValueError(f'Имя файла миграции не соответствует требованиям: {migration_file_path.name}')

                self._disk_migrations[
                    app_config.label, migration_file_path.name
                ] = parse_file_as(Migration, migration_file_path)

    def get_migrations(self) -> Generator[tuple[str, str, Migration], None, None]:
        for (app_label, migration_name), migration_obj in self._disk_migrations.items():
            yield app_label, migration_name, migration_obj
