from Database.DatabaseManager import DataBase
class LinkAccount:
    def __init__(self, client, player, initial_bytes):
        self.player = player
        self.client = client
        print(initial_bytes)
    def decode(self):
    	pass
    def process(self):
    	if self.player.link==0:
    		DataBase.replaceValue(self, "link", 1)
    		self.player.link=1