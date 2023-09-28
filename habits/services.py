import requests
from django.conf import settings

URL = 'https://api.telegram.org/bot'
TOKEN = settings.TG_TOKEN


def send_message(text, chat_id):
    requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': text
        }
    )
