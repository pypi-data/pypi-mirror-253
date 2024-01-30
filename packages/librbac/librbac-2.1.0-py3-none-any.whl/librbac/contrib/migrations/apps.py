from django.apps.config import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):

    name = __package__
    label = 'librbac_migrations'

    def _register_events(self):
        """Регистрация событий топика."""
        from librbac.config import rbac_config
        from librbac.contrib.migrations.domain.events import (
            PermissionMarkedObsolete)
        from librbac.contrib.migrations.domain.events import (
            PermissionsReplaced)
        from librbac.utils.rbac import get_rbac_topic_permission
        rbac_config.event_registry.register(
            get_rbac_topic_permission(),
            PermissionMarkedObsolete,
            PermissionsReplaced,
        )

    def ready(self):
        self._register_events()
