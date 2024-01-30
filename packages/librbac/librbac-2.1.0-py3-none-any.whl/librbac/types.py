from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING
from typing import Iterable
from typing import NamedTuple
from typing import Optional
from typing import Tuple
from typing import TypedDict
from typing import Union


if TYPE_CHECKING:
    from rest_framework.request import Request
    from rest_framework.viewsets import GenericViewSet


class PermissionGroup(NamedTuple):

    """Структура группы разрешений."""

    namespace: str
    resource: str


class Permission(NamedTuple):

    """Структура разрешения."""

    namespace: str
    resource: str
    action: str
    scope: Optional[str] = None


class TokenPermissionDict(TypedDict):

    """Структура разрешения передаваемого в составе токена."""

    resource_set_id: str
    """Объект доступа, например `auth:role`"""
    scopes: Iterable[str]
    """Операции на которые пользователю выдан доступ, например `read`"""
    exp: int
    """Временная метка после которой набор прав должен быть обновлён"""


TUser = Union['AbstractBaseUser', 'OIDCUser']
"""Тип "Пользователь системы"."""


class TRule(ABC):
    """Тип "Правило для проверки доступа"."""
    @abstractmethod
    def __call__(
        self,
        viewset: 'GenericViewSet',
        request: 'Request',
        user: TUser,
    ) -> bool:
        """Проверка доступа."""


TPermMapDict = dict[str, Tuple[Permission, ...]]
"""Структура сопоставления разрешений с действиями во ViewSet'е."""

