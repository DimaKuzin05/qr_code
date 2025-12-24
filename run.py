import os
import time

from dotenv import load_dotenv

from utils.config import BOT_DELAY
from utils.handlers import process_message
from utils.scheduler import start_scheduler
from utils.telegram_api import get_updates

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

offset = None

start_scheduler(TOKEN)

try:
    while True:
        updates = get_updates(TOKEN, offset)

        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            process_message(TOKEN, update["message"])

        time.sleep(BOT_DELAY)

except KeyboardInterrupt:
    print("Бот остановлен")
