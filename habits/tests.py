from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            email='test@test.com',
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('1234')
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {'email': 'test@test.com', 'password': "1234"}
        )
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.data = {
            "place": "Home",
            "time": "2023-09-27 19:00",
            "action": "test habit",
            "length": "100",
            "period": "1"
        }

    def test_create_habit(self):
        """Тестирование создания привычки"""
        response = self.client.post(
            reverse('habits:habit-create'),
            self.data
        )
        pk = Habit.objects.all().latest('pk').pk
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "place": "Home",
                "time": "2023-09-27T19:00:00Z",
                "action": "test habit",
                "nice_habit": False,
                "period": 1,
                "reward": None,
                "length": 100,
                "public": False,
                "owner": self.user.pk,
                "linked_habit": None
            }
        )

    def test_list_habit(self):
        """Тестирование вывода списка привычек"""
        self.test_create_habit()
        response = self.client.get(
            reverse('habits:habits-list')
        )
        pk = Habit.objects.all().latest('pk').pk

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [
                {
                    "id": pk,
                    "place": "Home",
                    "time": "2023-09-27T19:00:00Z",
                    "action": "test habit",
                    "nice_habit": False,
                    "period": 1,
                    "reward": None,
                    "length": 100,
                    "public": False,
                    "owner": self.user.pk,
                    "linked_habit": None
                }
            ]
        )

    def test_list_public_habit(self):
        """Тестирование вывода списка публичных привычек"""
        response = self.client.get(
            reverse('habits:public_habits-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(), [])

    def test_retrieve_habit(self):
        """Отображение одной привычки по ID"""
        self.test_create_habit()
        pk = Habit.objects.all().latest('pk').pk
        response = self.client.get(
            f'/habit/{pk}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "place": "Home",
                "time": "2023-09-27T19:00:00Z",
                "action": "test habit",
                "nice_habit": False,
                "period": 1,
                "reward": None,
                "length": 100,
                "public": False,
                "owner": self.user.pk,
                "linked_habit": None
            }
        )

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        self.test_create_habit()
        pk = Habit.objects.all().latest('pk').pk
        response = self.client.patch(
            f'/habit/update/{pk}/',
            {"period": "4"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "place": "Home",
                "time": "2023-09-27T19:00:00Z",
                "action": "test habit",
                "nice_habit": False,
                "period": 4,
                "reward": None,
                "length": 100,
                "public": False,
                "owner": self.user.pk,
                "linked_habit": None
            }
        )

    def habit_destroy(self):
        self.test_create_habit()
        pk = Habit.objects.all().latest('pk').pk
        response = self.client.delete(
            f'/habit/destroy/{pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_validate_HabitPeriodValidator(self):
        """Тестирование валидатора HabitPeriodValidator"""
        self.test_create_habit()
        pk = Habit.objects.all().latest('pk').pk
        response = self.client.patch(
            f'/habit/update/{pk}/',
            {"period": "10"}
        )

        self.assertEqual(
            response.json(),
            {
                "non_field_errors": [
                    "Переодичность не может быть больше 7 дней"
                ]
            }
        )

    def test_validate_HabitLengthValidator(self):
        """Тестирование валидатора HabitLengthValidator"""
        self.test_create_habit()
        pk = Habit.objects.all().latest('pk').pk
        response = self.client.patch(
            f'/habit/update/{pk}/',
            {"length": "210"}
        )

        self.assertEqual(
            response.json(),
            {
                "non_field_errors": [
                    "Продолжительность не может быть больше 120 секунд"
                ]
            }
        )
