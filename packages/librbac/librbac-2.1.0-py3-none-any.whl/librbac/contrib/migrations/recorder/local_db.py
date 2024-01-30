from ..models import MigrationRecord
from ..types import MigrationRecorderInterface


class MigrationRecorder(MigrationRecorderInterface):

    @property
    def migration_qs(self):
        return MigrationRecord.objects.all()

    @property
    def applied_migrations(self) -> tuple[tuple[str, str]]:
        return tuple(
            (migration.app, migration.name)
            for migration in self.migration_qs
        )

    def record_applied(self, app: str, name: str):
        """Record that a migration was applied."""
        self.migration_qs.create(app=app, name=name)

