from Utils.Writer import Writer
class MaintenanceMsg(Writer):
	def __init__(self, client, player):
		super().__init__(client)
		self.id = 20161
		self.player = player
	def encode(self):
		self.writeVint(1)