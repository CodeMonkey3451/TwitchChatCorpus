#!/usr/bin/python3

import json
import os
from os import listdir
from os.path import isfile, join
import logging
import requests
from requests import RequestException

from twitchutils import TwitchUtils


def fname2vID(fnamelist):
	"""Extract video IDs from filenames."""
	vIDlist = []
	for fname in fnamelist:
		vID = fname.split("_", 1)[0]
		vID = vID.replace("v", "")
		vIDlist.append(int(vID))
	return vIDlist


with open("../config.json", 'r', encoding="utf-8") as file:
    CONFIG = json.load(file)
usernames = CONFIG["usernames"]

"""Make a list of all existing logs, so we don't get already existing files.
Also check if output directory exists."""
LOGPATH = '../raw/'
if not os.path.exists(LOGPATH):
	os.makedirs(LOGPATH)
lognames = [f for f in listdir(LOGPATH) if isfile(join(LOGPATH, f))]
vIDlist = fname2vID(lognames)

LIMIT = 100 # Amount of results per page, set by 'getVodIds()' from 'twitchutils'

TU = TwitchUtils()
for name in usernames:
	videoIDs = []
	userID = TU.getuserID(name)

	"""Get all video IDs from the channel in increments of 'LIMIT' per page."""
	i = 0
	while True:
		newvideoIDs, nvideos = TU.getVodIds(userID, i, LIMIT)
		i += LIMIT
		for vID in newvideoIDs:
			vID = int(vID)
			videoIDs.append(vID)
			"""Only get video IDs that are not already downloaded."""
			if vID not in vIDlist:
				print(vID)
		if len(newvideoIDs) < LIMIT:
			break
