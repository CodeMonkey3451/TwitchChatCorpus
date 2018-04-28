import os
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

TRAINPATH = "./dialogs/"

def PrintQuestResp(question):
	"""Ask a question to get a respose. Print both."""
	response = chatbot.get_response(question)
	print("Bot: " + str(response))

with open("config.json", 'r', encoding="utf-8") as file:
    CONFIG = json.load(file)
ChatterBotName = CONFIG["ChatterBotName"]
ChatterBotDB = CONFIG["ChatterBotDatabase"]

# Define ChatterBot instance
chatbot = ChatBot(
    ChatterBotName,
    database = ChatterBotDB
)
chatbot.set_trainer(ListTrainer)

# Train based on the twitch conversations
directory = os.fsencode(TRAINPATH)
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	dirname = os.fsdecode(directory)
	if filename.endswith(".json"):
		with open(dirname + filename, "r", encoding="utf-8") as file:
			dialogs = json.load(file)
			for dia in dialogs:
				print(dia)
				chatbot.train(dia)

# Terminal interaction for testing
print("Write something to start...")
while True:
	try:
		userin = input("You: ")
		PrintQuestResp(userin)

    # Press ctrl-c or ctrl-d on the keyboard to exit
	except (KeyboardInterrupt, EOFError, SystemExit):
		break
