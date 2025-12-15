# scheduler задачи

import time
import schedule
from .report import send_daily_report  # относительный импорт

def start_scheduler(token, admin_id):
    schedule.every().day.at("23:55").do(send_daily_report, token, admin_id)

    while True:
        schedule.run_pending()
        time.sleep(1)

def send_morning_greeting(token, chat_id):
    with open("data/greetings.txt", encoding="utf-8") as f:
        text = f.read()

def send_massage(token, chat_id, text):
