from utils.telegram_api import send_document
from utils.config import ADMINS


def send_daily_report(token):
    path = "data/daily_report.txt"

    for admin_id in ADMINS:
        send_document(token, admin_id, path)