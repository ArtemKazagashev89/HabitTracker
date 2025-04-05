import requests

from config import settings


def send_telegram_message(chad_id, message):
    params = {
        "text": message,
        "chad_id": chad_id,
    }
    requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_API}/sendMessage", params=params)
