import requests

API_URL = "https://api.telegram.org/bot{}"


def get_updates(token, offset=None):
    """
    Получение обновлений через long polling
    """
    url = API_URL.format(token) + "/getUpdates"

    params = {"timeout": 100}

    if offset is not None:
        params["offset"] = offset

    try:
        resp = requests.get(url, params=params, timeout=120)
        return resp.json()

    except requests.exceptions.RequestException as err:
        # Telegram или сеть могут временно не отвечать — это нормально
        print(f"[telegram_api] get_updates error: {err}")
        return {"result": []}


def send_message(token, chat_id, text, parse_mode="Markdown"):
    """
    Отправка текстового сообщения
    """
    url = API_URL.format(token) + "/sendMessage"

    payload = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}

    requests.post(url, data=payload)


def send_photo(token, chat_id, photo_path):  # Отправка qr_code
    url = API_URL.format(token) + "/sendPhoto"

    with open(photo_path, "rb") as img:
        requests.post(url, data={"chat_id": chat_id}, files={"photo": img})


def send_document(token, chat_id, file_path, caption=None):  # отправка фейлов
    url = API_URL.format(token) + "/sendDocument"

    data = {"chat_id": chat_id}

    if caption:
        data["caption"] = caption
        data["parse_mode"] = "Markdown"

    with open(file_path, "rb") as f:
        requests.post(url, data=data, files={"document": f})
