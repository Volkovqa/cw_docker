from rest_framework import serializers

from habits.models import Habit


class LinkedAndRewardValidator:
    def __call__(self, value):
        linked_habit = bool(dict(value).get('linked_habit'))
        reward = bool(dict(value).get('reward'))

        if linked_habit and reward:
            raise serializers.ValidationError("Нельзя выбрать связанную привычку и вознагрождение одновременно")


class HabitLengthValidator:
    def __call__(self, value):
        length = dict(value).get('length')
        if isinstance(length, int) and length > 120:
            raise serializers.ValidationError("Продолжительность не может быть больше 120 секунд")


class LinkedIsNiceValidator:
    def __call__(self, value):
        linked_habit = dict(value).get('linked_habit')
        if linked_habit:
            habit = Habit.objects.get(pk=linked_habit.id)
            if not habit.nice_habit:
                raise serializers.ValidationError(
                    "В связанные привычка может быть только приятной привычки")


class NiceHabitValidator:
    def __call__(self, value):
        nice_habit = dict(value).get('nice_habit')
        linked_habit = bool(dict(value).get('linked_habit'))
        reward = bool(dict(value).get('reward'))

        if nice_habit and linked_habit or nice_habit and reward:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки")


class HabitPeriodValidator:
    def __call__(self, value):
        period = dict(value).get('period')
        if isinstance(period, int) and period > 7:
            raise serializers.ValidationError("Периодичность не может быть больше 7 дней")
