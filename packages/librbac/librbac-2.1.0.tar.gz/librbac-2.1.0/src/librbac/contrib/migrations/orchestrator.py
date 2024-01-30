from functools import cached_property
from typing import Generator
from typing import Iterable

from explicit.domain.model import asdict
from explicit.messagebus.events import Event
from pydantic.tools import parse_obj_as

from librbac.config import rbac_config
from librbac.types import Permission

from . import logger
from .domain.events import PermissionMarkedObsolete
from .domain.events import PermissionsReplaced
from .types import InvalidStateException
from .types import Migration
from .types import MigrationLoaderInterface
from .types import MigrationRecorderInterface
from .types import PermissionEntry
from .types import PermissionReplacementGraph


class ProjectedSystemState:

    """Прогнозируемое состояние системы, после применения миграций.

    Содержит только разрешения, с которыми выполнялись операции в миграциях.
    """

    _replacements_graph: PermissionReplacementGraph
    _obsolete: set[PermissionEntry]

    def __init__(self):
        self._replacements_graph = PermissionReplacementGraph()
        self._obsolete = set()

    def handle_replacement(self, replacements: list[PermissionEntry], replaces: list[PermissionEntry]):
        """Обработка замены разрешений."""
        if obsolete_replacements := self._obsolete.intersection(set(replacements)):
            raise InvalidStateException(f'Замены уже были помечены как устаревшие: {obsolete_replacements}.')
        if obsolete_replaced := self._obsolete.intersection(set(replaces)):
            raise InvalidStateException(f'Заменяемые разрешения уже были помечены как устаревшие: {obsolete_replaced}')

        self._replacements_graph.add_replacements(set(replacements), set(replaces))

    def handle_obsolescence(self, *obsolete: PermissionEntry):
        """Обработка устаревания разрешений."""
        obsolete = set(obsolete)
        if already_obsolete := obsolete.intersection(self._obsolete):
            raise InvalidStateException(f'Разрешения уже были помечены как устаревшие: {already_obsolete}')

        if already_replaced := obsolete.intersection(self._replacements_graph.internal_nodes):
            raise InvalidStateException(f'Разрешения уже были помечены как заменённые: {already_replaced}')

        self._obsolete.update(obsolete)

    def _entry_to_rbac_permission(self, permission_entry: PermissionEntry) -> Permission:
        return Permission(
            namespace=permission_entry.namespace,
            resource=permission_entry.resource,
            action=permission_entry.action,
            scope=permission_entry.scope
        )

    @property
    def available_permission_entries(self) -> set[Permission]:
        return {
            self._entry_to_rbac_permission(entry)
            for entry in self._replacements_graph.leaf_nodes - self._obsolete
        }

    @property
    def replaced_permission_entries(self) -> set[Permission]:
        return {
            self._entry_to_rbac_permission(entry)
            for entry in self._replacements_graph.internal_nodes
        }

    @property
    def obsolete_permission_entries(self) -> set[Permission]:
        return {
            self._entry_to_rbac_permission(entry)
            for entry in self._obsolete
        }


class EventGenerator:

    """Генератор набора событий из миграции."""

    _migration: Migration

    def __init__(self, migration: Migration):
        self._migration = migration

    def __iter__(self) -> 'Generator[Event]':
        for replaced_entry in self._migration.replaced:
            yield parse_obj_as(PermissionsReplaced, asdict(replaced_entry))
        for obsolete_entry in self._migration.obsolete:
            yield PermissionMarkedObsolete(permission=asdict(obsolete_entry))


class MigrationOrchestrator:
    """Выполняет общее управление процессом сборки и применения миграций."""

    _loader: MigrationLoaderInterface
    _recorder: MigrationRecorderInterface

    def __init__(self, loader: type[MigrationLoaderInterface], recorder: type[MigrationRecorderInterface]):
        self._loader = loader()
        self._recorder = recorder()

    @cached_property
    def _migrations(self) -> tuple[tuple[str, str, Migration], ...]:
        """Возвращает миграции."""
        return tuple(
            (app_label, migration_name, migration)
            for app_label, migration_name, migration in self._loader.get_migrations()
            if (app_label, migration_name) not in self._recorder.applied_migrations
        )

    def _build_projected_state(self, migrations: Iterable[Migration]) -> ProjectedSystemState:
        """Воссоздаёт ожидаемое состояние системы из миграций."""
        projected_system_state = ProjectedSystemState()
        for migration in migrations:
            for op in migration.replaced:
                projected_system_state.handle_replacement(replacements=op.replacements, replaces=op.replaces)
            projected_system_state.handle_obsolescence(*migration.obsolete)
        return projected_system_state

    def _verify_projected_state(self, projected_system_state: ProjectedSystemState):
        """Проверяет на противоречие состояния и кодовой базы."""
        from librbac.manager import rbac

        rbac_permissions = set(rbac.permissions)
        # убеждаемся, что устаревшие разрешения из миграций отсутствуют в системе
        if obsolete_in_rbac := projected_system_state.obsolete_permission_entries.intersection(rbac_permissions):
            raise Exception(f'Помеченный устаревшими разрешения всё еще существуют в системе: {obsolete_in_rbac}')
        # убеждаемся, что заменённые в миграциях разрешения отсутствуют в системе
        if replaced_in_rbac := projected_system_state.replaced_permission_entries.intersection(rbac_permissions):
            raise Exception(f'Помеченный заменёнными разрешения всё еще существуют в системе: {replaced_in_rbac}')
        # убеждаемся, что замены из миграций присутствуют в системе
        if replacements_not_in_rbac := projected_system_state.available_permission_entries.difference(rbac_permissions):
            Exception(f'Замены из миграций отсутствуют в системе: {replacements_not_in_rbac}')

    def apply_migrations(self, dry_run=False):
        """Применяет миграции."""

        logger.info('Формирование из миграций ожидаемого состояния системы...')
        projected_state: ProjectedSystemState = self._build_projected_state(
            tuple((migration for _, _, migration in self._migrations))
        )

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        logger.info(f'{len(projected_state.obsolete_permission_entries)} разрешений помечены как устаревшие.')
        for entry in projected_state.obsolete_permission_entries:
            logger.info(f'\t{entry}')

        logger.info(f'{len(projected_state.replaced_permission_entries)} разрешений заменены.')
        for entry in projected_state.replaced_permission_entries:
            logger.info(f'\t{entry}')
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        self._verify_projected_state(projected_state)
        logger.info('Выгрузка событий...')
        for app_label, migration_name, migration in self._migrations:
            for event in EventGenerator(migration):
                if not dry_run:
                    rbac_config.bus.handle(event)
                logger.info(f'\t{event}')
            if not dry_run:
                self._recorder.record_applied(app=app_label, name=migration_name)
