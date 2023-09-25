from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, PublicHabitListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [

    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habits-list'),
    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits-list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-retrieve'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-destroy'),
]
