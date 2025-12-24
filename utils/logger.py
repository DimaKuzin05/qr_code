import os
from datetime import datetime

FILE = "data/daily_report.txt"


def log_event(text):
    os.makedirs("data", exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {text}\n"

    with open(FILE, "a", encoding="utf-8") as f:
        f.write(line)
