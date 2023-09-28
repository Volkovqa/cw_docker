from datetime import datetime, timedelta

import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habit
from habits.services import send_message
from users.models import User


@shared_task
def get_message_data():
    """Отправка сообщения в телеграм"""
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=10)
    finish_time = time_now + timedelta(minutes=10)
    habits = Habit.objects.filter(time__gte=start_time).filter(time__lte=finish_time)

    for h in habits:
        action = h.action
        place = h.place
        time = h.time
        length = h.length
        username = h.owner.name
        user_tg = h.owner.telegram

        updates = get_updates()
        if updates['ok']:
            parse_updates(updates['result'])

        chat_id = User.objects.get(telegram=user_tg).chat_id

        text = "text"
        send_message(text, chat_id)

        h.time += timedelta(days=h.period)
        h.save()


def get_updates():
    """Получает chat_id"""
    token = settings.TG_TOKEN
    response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    return response.json()


def parse_updates(updates):
    for u in updates:
        user = User.objects.get(telgram=u["message"]['chat']['username'])
        if User.objects.filter(telegram=user).exist():
            user.chat_id = u['message']['chat']['id']
            user.update_id = u['update_id']
            user.save()