from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamStream2 import TeamStream2

class TeamChat(BSMessageReader):
	#14369
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player = player
		
	def decode(self):
		self.message = self.read_string()
		 
	def process(self):
		self.player.ctick += 1
		TeamStream2(self.client, self.player, self.message).send()