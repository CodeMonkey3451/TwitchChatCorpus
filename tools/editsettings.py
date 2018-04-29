#!/usr/bin/python3

import json

"""Edit the settings file used by Twitch-Chat-Downloader"""

with open("../config.json", 'r', encoding="utf-8") as file:
    CONFIG = json.load(file)
clientID = CONFIG["clientID"]

with open("settings.json", 'r', encoding="utf-8") as file:
    DATA = json.load(file)
DATA["client_id"] = clientID

with open("settings.json", 'w', encoding="utf-8") as file:
	json.dump(DATA, file, indent=4, ensure_ascii=False)