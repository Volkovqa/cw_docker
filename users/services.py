import requests
from django.conf import settings


class MyBot:
    """
    Класс для отправки сообщения через бот телеграм.
    """
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TG_TOKEN
    CHAT_ID = settings.CHAT_ID

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.CHAT_ID,
                'text': text
            }
        )