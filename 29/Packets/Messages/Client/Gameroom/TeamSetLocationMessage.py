from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class TeamSetLocationMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.player.map_id = self.read_Vint()


    def process(self):
        print(self.player.map_id)
        DataBase.replaceGameroomValue(self, 'mapID', self.player.map_id, "room")
        DataBase.loadGameroom(self)
        for i in self.plrData:
        	TeamGameroomDataMessage(self.client, self.player).sendWithLowID(i)