# обработка сообщения
from utils.qr import generate_qr
from utils.telegram_api import send_message, send_photo
from utils.users import save_user


def handle_message(token, message):
    chat_id = message["chat"]["id"]
    username = message["chat"].get("username", "unknown")
    text = message.get("text", "")

    save_user(chat_id, username)

    # /start
    if text == "/start":
        send_message(
            token,
            chat_id,
            "👋 *Привет!* Я бот для создания QR-кодов.\n\n"
            "Отправь мне ссылку — я превращу её в QR ",
        )

    # /me
    elif text == "/me":
        send_message(
            token,
            chat_id,
            f"❤️ *Твой профиль:*\nID: `{chat_id}`\nUsername: `{username}`",
        )

    # ссылка → QR
    elif text.startswith("http"):
        qr_path = generate_qr(text, chat_id)
        send_photo(token, chat_id, qr_path)

    # location
    elif "location" in message:
        lat = message["location"]["latitude"]
        lon = message["location"]["longitude"]
        send_message(
            token, chat_id, f"📍 *Ваша локация:*\nШирота: `{lat}`\nДолгота: `{lon}`"
        )

    else:
        send_message(token, chat_id, "❗ Я понимаю только ссылки и команды 🙂")
