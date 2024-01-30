from importlib import import_module
from typing import TYPE_CHECKING
from typing import Generator
from typing import Set
from typing import Type
from typing import Union

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from rest_framework.viewsets import GenericViewSet


if TYPE_CHECKING:
    from librbac.drf.viewsets import RBACMixin


def get_rbac_topic_permission() -> str:
    from django.conf import settings
    topic_attr = 'RBAC_PERMISSION_TOPIC'
    from librbac import default_settings
    topic_name = getattr(settings, topic_attr, None) or getattr(default_settings, topic_attr)
    if not topic_name:
        raise ImproperlyConfigured(
            f'Необходимо указать {topic_attr} в настройках.'
        )
    return topic_name


def get_all_viewsets(
    urlpatterns,
    viewsets=None
) -> Set[Type[GenericViewSet]]:
    """Находит и возвращает все ViewSet'ы системы."""
    viewsets = viewsets if viewsets is not None else set()
    for pattern in urlpatterns:
        if hasattr(pattern, 'url_patterns'):
            get_all_viewsets(pattern.url_patterns, viewsets=viewsets)
        else:
            if cls := getattr(pattern.callback, 'cls', None):
                if issubclass(cls, GenericViewSet):
                    viewsets.add(cls)

    return viewsets


def _get_rbac_viewsets() -> Generator[Union[GenericViewSet, 'RBACMixin'], None, None]:
    """Возвращает ViewSet'ы системы, доступ к которым нужно проверять."""
    from librbac.drf.viewsets import RBACMixin
    urlpatterns = import_module(settings.ROOT_URLCONF).urlpatterns
    for viewset in get_all_viewsets(urlpatterns):
        if issubclass(viewset, RBACMixin):
            yield viewset
