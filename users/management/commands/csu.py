from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания админа"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.ru",
            is_superuser=True,
            is_staff=True,
        )
        user.set_password('1234')
        user.save()
