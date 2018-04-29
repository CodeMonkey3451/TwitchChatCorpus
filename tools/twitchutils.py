"""Set of twitch API helper function."""
import json
import logging
import requests
from requests import RequestException

# APIs
TWITCH_TMI = 'http://tmi.twitch.tv/'
USERLIST_API = TWITCH_TMI + 'group/user/{}/chatters'

TWITCH_API = 'https://api.twitch.tv/'
OIDC_API = TWITCH_API + '/api/oidc/keys'

TWITCH_KRAKEN_API = TWITCH_API + 'kraken/'
CHANNEL_API = TWITCH_KRAKEN_API + 'channels/{}'
STREAMS_API = TWITCH_KRAKEN_API + 'streams/{}'
USER_EMOTE_API = TWITCH_KRAKEN_API + 'users/{}/emotes'
USER_ID_API = TWITCH_KRAKEN_API + 'users/{}'
USER_NAME_API = TWITCH_KRAKEN_API + 'users?login={}'
TWITCH_EMOTE_API = TWITCH_KRAKEN_API + 'chat/emoticon_images?emotesets=0'

TWITCH_VOD_API = CHANNEL_API + '/videos'

class TwitchUtils():
    """Twitch.tv API utility class."""

    def __init__(self):
        with open("../config.json", 'r', encoding="utf-8") as file:
            self.CONFIG = json.load(file)
        self.clientID = self.CONFIG["clientID"]

        self.TWITCH_API_COMMON_HEADERS = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': self.clientID,
            'Authorization': ''
        }

    def sanitizeUserName(self, username):
        """Format user name.

        Remove the @ if a string starts with it.
        """
        if username.startswith("@"):
            username = username[1:]  # remove "@"
        return username.lower()


    def getJSONObjectFromTwitchAPI(self, url):
        """Get and handle JSON object from Twitch API."""
        try:
            r = requests.get(url, headers=self.TWITCH_API_COMMON_HEADERS)
            r.raise_for_status()
            return r.json()

        except RequestException as e:
            # 4xx/5xx errors from server

            msg = "Twitch server-side error, URL sent is {}, status code is {}".format(url, r.status_code)
            msg += "\nError message from twitch's JSON {} ".format(r.json())
            raise RequestException(msg)

        except ValueError as e:
            # likely can't parse JSON
            msg = "Error in getting user JSON with URL {}, status code is {}".format(url, r.status_code)
            raise ValueError(msg)


    def getUserDataFromID(self, user_id):
        """Get Twitch user data of a given id."""
        url = USER_ID_API.format(user_id)
        data = self.getJSONObjectFromTwitchAPI(url)

        u_name = sanitizeUserName(data["name"])
        display_name = data["display_name"]
        id = data["_id"]

        return data


    def getuserTag(self, username):
        """Get the full data of user from username."""
        url = USER_NAME_API.format(username)
        return self.getJSONObjectFromTwitchAPI(url)


    def getuserID(self, username):
        """Get the twitch id (numbers) from username."""
        u_name = self.sanitizeUserName(username)

        logging.info("User data not in cache when trying to access user ID. User tag {}".format(username))

        try:
            data = self.getuserTag(username)
            id = data["users"][0]["_id"]
            display_name = data["users"][0]["display_name"]

            return id

        except (ValueError, KeyError) as e:
            logging.info("Cannot get user info from API call, can't get user ID of {}".format(username))
            raise e

        except (IndexError, RequestException):
            logging.info("Seems no such user as {}".format(username))
            raise UserNotFoundError("No user with login id of {}".format(username))


    def getUserDataFromID(self, user_id):
        """Get Twitch user data of a given id."""
        url = USER_ID_API.format(user_id)
        data = self.getJSONObjectFromTwitchAPI(url)

        u_name = self.sanitizeUserName(data["name"])
        display_name = data["display_name"]
        id = data["_id"]

        return data


    def getVodObject(self, channelID, page = 0, limit = 10):
        """Get Twitch VOD object from channel id and a specific page.
        Limit sets the amount of results per page (maximum is 100)."""
        url = TWITCH_VOD_API.format(channelID)

        url += '?limit={0}&offset={1}'.format(limit, page)

        return self.getJSONObjectFromTwitchAPI(url)


    def getVodIds(self, channelID, page = 0, limit = 10):
        """Get Twitch VOD IDs from channel id and a specific page.
        Second return is maximum pages (including 0)."""
        obj = self.getVodObject(channelID, page, limit)
        videoIDs = []
        for videos in obj["videos"]:
            videoIDs.append(int(videos["_id"].replace("v", "")))
        nvideos = obj["_total"]
        return videoIDs, nvideos
