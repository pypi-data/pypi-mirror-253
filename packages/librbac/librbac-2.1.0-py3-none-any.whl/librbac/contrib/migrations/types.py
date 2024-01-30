from abc import ABCMeta
from abc import abstractmethod
from itertools import product
from typing import TYPE_CHECKING
from typing import Generator

from pydantic import BaseModel
from pydantic import conlist
from pydantic import root_validator


if TYPE_CHECKING:
    from dataclasses import dataclass  # noqa



else:
    from pydantic.dataclasses import dataclass  # noqa


@dataclass(frozen=True)
class PermissionEntry:

    """Запись о разрешении в миграции."""

    namespace: str
    resource: str
    action: str
    title: str
    module: str
    scope: str | None = None


@dataclass(frozen=True)
class ReplacedEntry:

    """Запись о замене разрешений в миграции."""

    replacements: conlist(PermissionEntry, min_items=1)
    replaces: conlist(PermissionEntry, min_items=1)


class Migration(BaseModel):

    """Миграция разрешений."""

    description: str
    replaced: conlist(ReplacedEntry, min_items=0)
    obsolete: conlist(PermissionEntry, min_items=0)

    @root_validator
    def check_has_operations(cls, values):
        assert values['replaced'] or values['obsolete'], 'Миграция должна содержать хотя-бы одну операцию'
        return values


class InvalidStateException(BaseException):
    """Нарушена целостность состояния."""


class PermissionReplacementGraph:

    """Хранилище замен разрешений в виде графа."""

    def __init__(self):
        self._graph = {}

    def _add_permission(self, entry: PermissionEntry):
        """Добавляет в граф новый узел разрешения, если он еще не существует."""
        if entry not in self._graph:
            self._graph[entry] = set()

    def add_replacements(self, replacements: set[PermissionEntry], replaces: set[PermissionEntry]):
        """Добавляет замену разрешений."""

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if invalid_replacements := self.internal_nodes.intersection(replacements):
            raise InvalidStateException(f'Некорректная замена: {invalid_replacements}')
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        for replacement, replaced in product(replacements, replaces):
            self._add_permission(replaced)
            self._add_permission(replacement)
            self._graph[replaced].add(replacement)

    def __contains__(self, item: PermissionEntry):
        return item in self._graph

    def __getitem__(self, item: PermissionEntry) -> set[PermissionEntry]:
        """Получение заменяемых разрешений по экземпляру замены."""
        return {entry for entry, replaced_by in self._graph.items() if item in replaced_by}

    @property
    def internal_nodes(self) -> set[PermissionEntry]:
        """Набор разрешений, которые должны быть удалены из системы после применения миграций."""
        return {node for node in self._graph if self._graph[node]}

    @property
    def leaf_nodes(self) -> set[PermissionEntry]:
        """Набор разрешений, которые должны быть в системе после применения миграций."""
        return {node for node in self._graph if not self._graph[node]}


class MigrationRecorderInterface(metaclass=ABCMeta):
    """Интерфейс регистратора миграций."""

    @property
    @abstractmethod
    def applied_migrations(self) -> tuple[tuple[str, str]]:
        """Возвращает сопоставление всех применённых миграций по приложениям."""

    @abstractmethod
    def record_applied(self, app: str, name: str):
        """Регистрирует миграцию как применённую."""


class MigrationLoaderInterface(metaclass=ABCMeta):
    """Интерфейс загрузчика миграций разрешений."""

    @abstractmethod
    def get_migrations(self) -> Generator[tuple[str, str, Migration], None, None]:
        """Возвращает все доступные миграции."""


