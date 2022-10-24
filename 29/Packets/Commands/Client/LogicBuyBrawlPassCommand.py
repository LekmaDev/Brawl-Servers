from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class LogicBuyBrawlPassCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        	DataBase.replaceValue(self, "bpUnlock", 1)
        	newGems = self.player.gems - 169
        	DataBase.replaceValue(self, 'gems', newGems)


