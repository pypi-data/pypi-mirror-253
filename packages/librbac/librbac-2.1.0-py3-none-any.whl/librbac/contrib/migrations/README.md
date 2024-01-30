# Модуль поддержки миграций разрешений для общей библиотеки контроля доступа.

## Подключение
settings.py:
```python

INSTALLED_APPS = [
    # другие приложения
    'librbac',
    'librbac.contrib.migrations',
]
```


testapp/apps.py:
```python

from django.apps.config import AppConfig as AppConfigBase

from librbac.contrib.migrations.domain.events import PermissionsReplaced
from librbac.contrib.migrations.domain.events import PermissionMarkedObsolete


class AppConfig(AppConfigBase):

    name = __package__

    def _register_event_handlers(self):
        """Регистрация обработчиков событий."""
    from testapp.core import bus
    # обработчик с публикацией событий в межсервисную шину
    from librbac.contrib.migrations.services.handlers import publish_to_adapter

    for event, handler in (
        (PermissionsReplaced, publish_to_adapter),
        (PermissionMarkedObsolete, publish_to_adapter),
    ):
        bus.add_event_handler(event, handler)
```
                

testapp/permissions/migrations/0001_initial.json
```json
{
  "description":  "Описание миграции.",
  "replaced": [
    {
      "replacements": [
        {
          "namespace": "test",
          "resource": "person",
          "action": "write",
          "scope": "own",
          "title": "Редактирование своего ФЛ",
          "module": "Администрирование"
        }
      ],
      "replaces": [
        {
          "namespace": "test",
          "resource": "person",
          "action": "write",
          "title": "Редактирование ФЛ",
          "module": "Администрирование"
        }
      ]
    }
  ],
  "obsolete": [
    {
      "namespace": "test",
      "resource": "person",
      "action": "delete",
      "title": "Удаление ФЛ",
      "module": "Администрирование"
    }
  ]
}
```
