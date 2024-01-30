from librbac.backends.base import BackendBase
from librbac.events import PermissionPushed


class LocalBackend(BackendBase):

    """Бэкенд RBAC с публикацией разрешений в локальную шину."""

    def push_permission(self, event: 'PermissionPushed'):
        from librbac.config import rbac_config
        rbac_config.bus.handle(event)
