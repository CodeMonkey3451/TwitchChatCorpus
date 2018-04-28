#!/bin/bash

TCD_DIR="/home/alex/Workspace/ChatBotProject/Twitch-Chat-Downloader"

re='^[0-9]+$'

# Set directories
ROOT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
RAW_DIR="$ROOT_DIR/raw"

TOOLS_DIR="$ROOT_DIR/tools"

cd "$TOOLS_DIR"
python3 getvideoids.py |
 	while IFS= read -r line
  	cd "$TCD_DIR"
  	do
  		if [[ $line =~ $re ]]
      	then
    		python3 app.py -v "$line" --format bot --output "$RAW_DIR"
    	else
    		exit 1
    	fi
  	done

cd ..
