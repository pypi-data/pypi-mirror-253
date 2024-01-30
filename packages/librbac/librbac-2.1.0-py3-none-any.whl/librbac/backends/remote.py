from typing import TYPE_CHECKING

from django.utils.functional import cached_property

from librbac.backends.base import BackendBase
from librbac.events import PermissionPushed


if TYPE_CHECKING:
    from librbac.events import PermissionPushed


class RemoteBackend(BackendBase):

    """Бэкенд RBAC с публикацией разрешений в межсервисную шину."""

    @cached_property
    def _rbac_topic_permission(self) -> str:
        from librbac.utils.rbac import get_rbac_topic_permission
        return get_rbac_topic_permission()

    def push_permission(self, event: 'PermissionPushed'):
        from librbac.config import rbac_config
        rbac_config.adapter.publish(
            self._rbac_topic_permission,
            event.dump()
        )

