from Database.DatabaseManager import DataBase
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Utils.Reader import BSMessageReader

class TeamMemberStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.state = self.read_Vint()
        self.player.pin = self.read_Vint()
        self.player.mode = self.read_Vint()

    def process(self):
        DataBase.UpdateGameroomPlayerInfo(self, self.player.low_id)
        DataBase.loadGameroom(self)
        self.player.ctick += 1
        for i in self.plrData:
            TeamGameroomDataMessage(self.client, self.player).sendWithLowID(self.plrData[i]["lowID"])