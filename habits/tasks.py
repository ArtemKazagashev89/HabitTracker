from celery import shared_task

from .services import send_telegram_message


@shared_task
def send_reminder(chat_id, habit_description):
    message = f"Напоминание: {habit_description}"
    send_telegram_message(chat_id, message)
