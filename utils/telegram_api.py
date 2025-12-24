import requests

BASE_URL = "https://api.telegram.org/bot"


def get_updates(token, offset=None):
    url = BASE_URL + token + "/getUpdates"

    params = {"timeout": 100}
    if offset is not None:
        params["offset"] = offset

    r = requests.get(url, params=params)
    return r.json()


def send_message(token, chat_id, text):
    url = BASE_URL + token + "/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    requests.post(url, data=data)


def send_photo(token, chat_id, photo_path):
    url = BASE_URL + token + "/sendPhoto"

    with open(photo_path, "rb") as photo:
        requests.post(
            url,
            data={"chat_id": chat_id},
            files={"photo": photo}
        )