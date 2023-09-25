from habits.models import Habit
from rest_framework import serializers


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [

        ]
