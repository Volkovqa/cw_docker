from django.conf import settings
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

PERIOD = [
    ('EVERY DAY', 'раз в день'),
    ('EVERY OTHER DAY', 'через день'),
    ('EVERY WEEK', 'раз в неделю'),
]


class Habit(models.Model):
    """Модель привычки"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Пользователь",
                              **NULLABLE)

    place = models.CharField(max_length=150, verbose_name='Место', **NULLABLE)
    time = models.TimeField(verbose_name="Время", **NULLABLE)
    action = models.CharField(max_length=100, verbose_name="Действие")
    nice_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    linked_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Связанная приывычка", **NULLABLE)
    period = models.CharField(max_length=100, default='EVERY_DAY', choices=PERIOD, verbose_name="Периодичность")
    reward = models.CharField(max_length=150, verbose_name="Вознаграждение", **NULLABLE)
    length = models.SmallIntegerField(verbose_name="Продолжительность")
    public = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return f"Habit - {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"