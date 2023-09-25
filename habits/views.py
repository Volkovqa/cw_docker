from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания урока"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Контроллер для просмотра привычек пользователя"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """Контроллер для просмотра публичных привычек"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра одной привычки по id"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Изменение данных привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
