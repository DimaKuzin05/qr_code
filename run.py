import os
import time

from dotenv import load_dotenv

from utils.handlers import handle_message
from utils.telegram_api import get_updates

load_dotenv()

ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
TOKEN = os.getenv("BOT_TOKEN")

offset = None

try:
    while True:
        updates = get_updates(TOKEN, offset)

        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            if "message" in update:
                handle_message(TOKEN, update["message"])

        time.sleep(1)

except KeyboardInterrupt:
    print("\nБот остановлен корректно 👍")
