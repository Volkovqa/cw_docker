from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.url = '/users/user/'
        self.data = {
            'email': 'test@mail.ru',
            'password': '1234'
        }

    def test_create_user(self):
        """Тестирование создания пользователя"""

        response = self.client.post(
            f"{self.url}",
            data=self.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.all()[0].email,
            'test@mail.ru'
        )

    def test_csu_command(self):
        """Тестирование кастомной команды для создания супер пользователя"""
        call_command('csu')
        user = User.objects.all()[0]
        self.assertEqual(
            user.email,
            'admin@mail.ru'
        )

        self.assertTrue(
            user.is_superuser
        )
