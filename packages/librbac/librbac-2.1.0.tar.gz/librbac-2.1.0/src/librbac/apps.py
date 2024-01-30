from django.apps.config import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):

    name = __package__

    def _register_events(self):
        """Регистрация событий топика."""
        from librbac.config import rbac_config
        from librbac.events import PermissionPushed
        from librbac.utils.rbac import get_rbac_topic_permission
        rbac_config.event_registry.register(
            get_rbac_topic_permission(),
            PermissionPushed,
        )

    def ready(self):
        self._register_events()
