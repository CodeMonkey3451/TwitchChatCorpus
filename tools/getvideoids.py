
import json
import logging
import requests
from requests import RequestException

from twitchutils import TwitchUtils

TU = TwitchUtils()
userID = TU.getuserID("zetalot")

videoIDs, npages = TU.getVodIds(userID, 0)
for vID in videoIDs:
    print(vID)

i = 0
while True:
    i += 10
    newvideoIDs, n = TU.getVodIds(userID, i)
    for vID in newvideoIDs:
        videoIDs.append(vID)
        print(vID)
    if len(newvideoIDs) < 10:
        break
