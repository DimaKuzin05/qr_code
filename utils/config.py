import json
import os

import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

yaml_path = os.path.join(BASE_DIR, "config.yaml")
json_path = os.path.join(BASE_DIR, "config.json")

with open(yaml_path, "r", encoding="utf-8") as f:
    yaml_config = yaml.safe_load(f)

with open(json_path, "r", encoding="utf-8") as f:
    json_config = json.load(f)

ADMINS = yaml_config["admins"]
BOT_DELAY = yaml_config["bot"]["delay"]

MESSAGES = json_config["messages"]

OPENWEATHER_API_KEY = yaml_config.get("openweather_api_key", "")