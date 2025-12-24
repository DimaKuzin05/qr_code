import csv
import os
from datetime import datetime

FILE = "data/users.csv"


def save_user(message):
    os.makedirs("data", exist_ok=True)

    chat = message["chat"]
    chat_id = chat["id"]
    name = chat.get("first_name", "")

    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["chat_id", "name", "date"])

    with open(FILE, "r", encoding="utf-8") as f:
        if str(chat_id) in f.read():
            return

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([chat_id, name, datetime.now().date()])
