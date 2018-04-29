**TwitchChatCorpus**
===============
Extract [Twitch](https://www.twitch.tv/) chat conversations from VOD chatlogs to train a [ChatterBot](https://github.com/gunthercox/ChatterBot) instance.

Utility functions derived from https://github.com/NMisko/monkalot.

#### Setup:
* install `requirements.txt`
* Get the [Twitch-Chat-Downloader](https://github.com/PetterKraabol/Twitch-Chat-Downloader)

#### Configuration:
Make sure to modify the following values in `config.json`:
- `Twitch-Chat-Downloader_directory`: Where you setup Twitch-Chat-Downloader
- `clientID`: Twitch ClientID for API calls
- `usernames`: Twitch usernames you want to get the chat logs from
- `ignore_list`: Conversations of these users will be ignored (E.g. bots)
- `banphrases`: Conversations containing these strings will be ignored
- `ChatterBotName`: Name of the ChatterBot instance
- `ChatterBotDatabase`: Name of the database for the ChatterBot instance

#### Usage:
1. Use `getlogs.sh` to download Twitch VOD logs to `./raw`.
2. Execute `python3 log2conv.py` to extract conversations from the raw logs to `./dialogs`.
3. Train a [ChatterBot](https://github.com/gunthercox/ChatterBot) instance with `python3 train_twitch.py`.
