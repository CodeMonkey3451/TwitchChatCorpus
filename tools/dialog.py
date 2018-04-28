class Dialog():
	"""Builds a conversation between two users."""
	def __init__(self, sender, target, msg):
		"""Initialize usernames and dialog corpus."""
		self.user = [sender, target]
		self.lastsend = 0 # Last person to send a message
		self.corpus = [msg.strip()] # Dialog corpus


	def usersDialog(self, sender, target):
		"""Check if sender and target are part of the dialog."""
		return all(x in self.user for x in [sender, target])


	def getLength(self):
		"""Return the length of the message corpus."""
		return len(self.corpus)


	def getIdx(self, name):
		"""Return index (0 or 1) for a username."""	
		return self.user[1] == name


	def addMsg(self, sender, target, msg):
		"""Add a new msg to the dialog corpus."""
		msg = msg.strip()

		"""Check who last send a message and either append
		the message or create a new message field."""
		if self.user[self.lastsend] == sender:
			self.corpus[-1] += " " + msg
		else:
			self.corpus.append(msg)
			self.lastsend = self.getIdx(sender)


	def arrayOut(self):
		"""Transform the dialog corpus to an anonymous array for output."""

		return self.corpus
