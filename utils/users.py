# работа с csv

import csv
import os

FILE_PATH = "data/users.csv"


def save_user(chat_id, username):
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["chat_id", "username"])

    with open(FILE_PATH, "r", newline="") as f:
        users = [row[0] for row in csv.reader(f)]

    if str(chat_id) not in users:
        with open(FILE_PATH, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([chat_id, username])
