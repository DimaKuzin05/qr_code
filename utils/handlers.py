import json

from utils.telegram_api import send_message, send_photo, send_photo_url
from utils.qr import generate_qr
from utils.users import save_user
from utils.config import ADMINS, MESSAGES
from utils.catass import get_random_cat
from utils.location import get_address


def main_keyboard():
    return json.dumps({
        "keyboard": [
            ["QR", "!Кота"],
            ["/me", "/admin"]
        ],
        "resize_keyboard": True
    })


def process_message(token, message):
    chat_id = message["chat"]["id"]
    save_user(message)

    # Геолокация (OpenWeather)
    if "location" in message:
        lat = message["location"]["latitude"]
        lon = message["location"]["longitude"]

        address = get_address(lat, lon)

        send_message(
            token,
            chat_id,
            "Ваше местоположение:\n" + address
        )
        return

    # Фото от пользователя
    if "photo" in message:
        send_message(token, chat_id, "Я получил изображение 📷")
        return

    if "text" not in message:
        return

    text = message["text"].strip()

    # start
    if text == "/start":
        send_message(
            token,
            chat_id,
            MESSAGES["start"],
            reply_markup=main_keyboard()
        )
        return

    # кнопка QR
    if text == "QR":
        send_message(token, chat_id, "Отправь ссылку, и я сделаю QR-код")
        return

    # кнопка кота
    if text == "!Кота":
        cat_url = get_random_cat()
        send_photo_url(token, chat_id, cat_url)
        send_message(token, chat_id, "Держи кота 🐱")
        return

    # /me
    if text == "/me":
        send_message(token, chat_id, f"Ваш chat_id: {chat_id}")
        return

    # /admin
    if text == "/admin":
        if chat_id in ADMINS:
            send_message(token, chat_id, "Вы администратор")
        else:
            send_message(token, chat_id, "Нет доступа")
        return

    # ссылка → QR
    if "http://" in text or "https://" in text:
        qr_path = generate_qr(text)
        send_photo(token, chat_id, qr_path)
        send_message(token, chat_id, "QR-код готов ✅")
        return

    send_message(token, chat_id, MESSAGES["unknown"])