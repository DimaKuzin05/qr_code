import os
import time

import qrcode


def generate_qr(text):
    os.makedirs("temp", exist_ok=True)

    filename = f"temp/qr_{int(time.time())}.png"
    img = qrcode.make(text)
    img.save(filename)

    return filename
