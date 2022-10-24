from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase

class TeamKick(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
    	self.read_Vint()#highID
    	self.ID = self.read_Vint()#lowID
    def process(self):
    	DataBase.leaveFromRoom(self, self.ID)
    	DataBase.replaceOtherValue(self, self.ID, "roomID", 0)
    	TeamGameroomDataMessage(self.client, self.player).send()