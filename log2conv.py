"""Extract conversation from chat logs."""

import os
import json
from tools.logparse import LogParse

LOGPATH = './raw/'
TRAINPATH = './dialogs/'

"""Iterate through all available logs."""
directory = os.fsencode(LOGPATH)
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	dirname = os.fsdecode(directory)
	if filename.endswith(".txt"):
		print(filename)
		f = open(dirname + filename)
		parser = LogParse(f)
		dialoglist = parser.getDialogs()

		logname = filename.replace(".txt", "") + ".json"
		with open(TRAINPATH + logname, 'w', encoding="utf-8") as file:
			json.dump(dialoglist, file, indent=4, ensure_ascii=False)
