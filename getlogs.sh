#!/bin/bash

# Get Twitch.tv VOD IDs with 'getvideoids.py' and
# execute 'Twitch-Chat-Downloader' for each ID.

# Function to read values of a json file
function readJson {  
  UNAMESTR=`uname`
  if [[ "$UNAMESTR" == 'Linux' ]]; then
    SED_EXTENDED='-r'
  elif [[ "$UNAMESTR" == 'Darwin' ]]; then
    SED_EXTENDED='-E'
  fi; 

  VALUE=`grep -m 1 "\"${2}\"" ${1} | sed ${SED_EXTENDED} 's/^ *//;s/.*: *"//;s/",?//'`

  if [ ! "$VALUE" ]; then
    echo "Error: Cannot find \"${2}\" in ${1}" >&2;
    exit 1;
  else
    echo $VALUE ;
  fi; 
}

# Define regular expression
re='^[0-9]+$'

# Set directories
ROOT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
RAW_DIR="$ROOT_DIR/raw"
TOOLS_DIR="$ROOT_DIR/tools"
TCD_DIR=`readJson config.json Twitch-Chat-Downloader_directory`

cd "$TOOLS_DIR"
# Update settings.json and copy it to Twitch-Chat-Downloader-directory:
python3 editsettings.py
cp "$TOOLS_DIR/settings.json" "$TCD_DIR/settings.json"

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
