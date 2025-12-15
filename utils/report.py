import os
from datetime import datetime

from .telegram_api import send_document

REPORT_PATH = "data/daily_report.txt"


def write_report_line(text: str):
    """
    Добавляет строку в daily_report.txt
    Используется для логирования событий бота
    """
    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")


def send_daily_report(token: str, admin_ids: list[int]):
    """
    Отправляет daily_report.txt всем администраторам
    """
    os.makedirs("data", exist_ok=True)

    # если файл пустой или не существует
    if not os.path.exists(REPORT_PATH) or os.path.getsize(REPORT_PATH) == 0:
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write("Отчет за день пуст. Активность отсутствует.\n")

    for admin_id in admin_ids:
        send_document(
            token=token,
            chat_id=admin_id,
            file_path=REPORT_PATH,
            caption="📊 *Отчет о работе бота за день*",
        )
