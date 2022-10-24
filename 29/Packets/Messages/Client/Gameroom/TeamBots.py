from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

class TeamBotsMsg(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
    	self.bot = self.read_int()
    def process(self):
    	TeamGameroomDataMessage(self.client, self.player).send()
    	