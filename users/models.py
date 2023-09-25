from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {
    'null': True,
    'blank': True
}


class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    telegram = models.CharField(unique=True, verbose_name='telegram', **NULLABLE)
    chat_id = models.PositiveIntegerField(default=0, verbose_name='Номер чата', **NULLABLE)
    update_id = models.PositiveIntegerField(default=0, verbose_name='Номер последнего сообщения', **NULLABLE)
    name = models.CharField(max_length=50, verbose_name="Имя", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
