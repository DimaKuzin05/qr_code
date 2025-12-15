from datetime import datetime

REPORT_PATH = "data/daily_report.txt"


def log_event(text):
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] {text}\n")
