import json
import time
from threading import Thread

import schedule

from utils.config import ADMINS
from utils.report import send_daily_report


def start_scheduler(token):
    with open("tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)

    time_str = tasks["daily_report"]["time"]

    schedule.every().day.at(time_str).do(send_daily_report, token)

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(1)

    Thread(target=loop, daemon=True).start()
