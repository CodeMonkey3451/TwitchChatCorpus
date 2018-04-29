import json
import logging
import requests
from requests import RequestException

from twitchutils import TwitchUtils

with open("../config.json", 'r', encoding="utf-8") as file:
    CONFIG = json.load(file)
usernames = CONFIG["usernames"]

TU = TwitchUtils()
for name in usernames:
	userID = TU.getuserID(name)

	videoIDs, nvideos = TU.getVodIds(userID, 0)
	for vID in videoIDs:
		print(vID)

	"""Get all video IDs from the channel in increments of 10 per page."""
	i = 0
	while True:
	    i += 10
	    newvideoIDs, nvideos = TU.getVodIds(userID, i)
	    for vID in newvideoIDs:
	        videoIDs.append(vID)
	        print(vID)
	    if len(newvideoIDs) < 10:
	        break
