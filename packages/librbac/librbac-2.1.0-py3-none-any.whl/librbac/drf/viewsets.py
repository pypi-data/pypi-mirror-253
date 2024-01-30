from typing import TYPE_CHECKING
from typing import Union

from django.utils.decorators import classonlymethod

from librbac.drf.permissions import HasAccess
from librbac.types import Permission
from librbac.types import TPermMapDict


if TYPE_CHECKING:
    from rest_framework.viewsets import GenericViewSet


class RBACMixin:

    """Примесь для ViewSet'ов требующих контроля доступа."""

    perm_map: TPermMapDict
    """Сопоставление ViewSet'а и требуемых разрешений."""

    permission_classes = (
        HasAccess,
    )

    @classonlymethod
    def as_view(cls: Union['GenericViewSet', 'RBACMixin'], actions=None, **initkwargs):
        assert isinstance(cls.perm_map, dict)
        assert len(cls.perm_map)
        for action, perms in cls.perm_map.items():
            assert all(isinstance(p, Permission) for p in perms)
        return super().as_view(actions=actions, **initkwargs)
