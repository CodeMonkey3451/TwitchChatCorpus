import json
from tools.dialog import Dialog

class LogParse():
	"""Parse a log for dialogs and save them in a list anonymously."""
	def getDialoglist(self):
		return self.dialoglist


	def getDialogs(self):
		"""Only returns 'real' dialogs, where both persons said something as arrays."""
		dialogs = []
		for dia in self.dialoglist:
			if dia.getLength() > 1:
				dialogs.append(dia.arrayOut())
		return dialogs


	def addToDialoglist(self, user, target, msg):
		"""Add a new message to an existing dialog
		or create a new one."""

		for dialog in self.dialoglist:
			if dialog.usersDialog(user, target):
				dialog.addMsg(user, target, msg)
				return

		newDialog = Dialog(user, target, msg)
		self.dialoglist.append(newDialog)


	def analyze_log(self, log):
		"""Parse log file and add dialogs to list."""
		for line in log:
			parts = line.split(":", 1)
			user = parts[0].strip().lower()
			msg = parts[1].strip()

			"""Check if only one '@' is in the string.
			Remove the '@username' part."""
			if "@" in msg:
				target = msg.split("@", 1)[1]
				if "@" not in target:
					target = target.split(" ", 1)[0]
					if target.lower() not in self.ignorelist:
						crop_msg = msg.replace("@{}".format(target), "").strip()

						self.addToDialoglist(user, target.lower(), crop_msg)


	def __init__(self, log):
		with open("config.json", 'r', encoding="utf-8") as file:
			self.CONFIG = json.load(file)
		self.ignorelist = self.CONFIG["ignore_list"]

		self.dialoglist = []
		self.analyze_log(log)
