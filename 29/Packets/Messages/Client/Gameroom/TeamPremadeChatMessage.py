from Database.DatabaseManager import DataBase
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamStream import TeamStream

class TeamPremadeChatMessage(BSMessageReader):
    #14369
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player
        
    def decode(self):
        print(f"[INFO] TeamPremadeChatMessage send! Pin: {self.read_Vint()} Mode: {self.player.mode}")
        self.player.pin = self.read_Vint()
        self.player.mode = self.read_Vint()
         
    def process(self):
        #self.player.pin = self.pin
        self.player.ctick += 1
        TeamStream(self.client, self.player).send()