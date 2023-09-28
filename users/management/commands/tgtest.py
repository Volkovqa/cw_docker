from django.core.management import BaseCommand

from habits.services import send_message


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_message("Тестовый текст", 303384091)
