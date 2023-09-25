from habits.models import Habit
from rest_framework import serializers

from habits.validators import HabitLengthValidator, NiceHabitValidator, LinkedAndRewardValidator, LinkedIsNiceValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitLengthValidator, NiceHabitValidator, LinkedAndRewardValidator, LinkedIsNiceValidator
        ]
