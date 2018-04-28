**TwitchChatCorpus**
===============
Extract [Twitch](https://www.twitch.tv/) chat conversations from VOD chatlogs to train a [ChatterBot](https://github.com/gunthercox/ChatterBot) instance.

Utility functions derived from https://github.com/NMisko/monkalot.

#### Setup:
* install `requirements.txt`
* Get the [Twitch-Chat-Downloader](https://github.com/PetterKraabol/Twitch-Chat-Downloader)

#### Configuration:
Make sure to modify the following values in `config.json`:
- `clientID`: Twitch ClientID for API calls.
- `ignore_list`: Conversations of these users will be ignored. (E.g. bots)

#### Usage:
1. Use `getlogs.sh` to download Twitch VOD logs to `./raw`
2. Execute `log2conv.py` to extract conversations from the raw logs to `./dialogs`.
3. Train a [ChatterBot](https://github.com/gunthercox/ChatterBot) instance with `train_twitch.py`
