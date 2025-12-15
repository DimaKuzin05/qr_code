# генерация qr-кода

import os

import qrcode


def generate_qr(text, chat_id):
    os.makedirs("temp", exist_ok=True)
    path = f"temp/qr_{chat_id}.png"
    with open(path, "wb") as f:
        img = qrcode.make(text)
        img.save(f)
    return path
