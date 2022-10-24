from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Packets.Messages.Server.ServerError import ServerErrorMessage
from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
from Database.DatabaseManager import DataBase

class TeamSearch(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        print(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
    	#14199!!!#
    	self.mapslot = self.read_Vint()
    def process(self):
    	DataBase.getRandomroomAndJoin(self, self.mapslot)
    	if self.player.room_id and self.playerCount <=2:
    		DataBase.replaceValue(self, "roomID", self.player.room_id)
    		DataBase.loadGameroom(self)
    		for i in self.plrData:
    			TeamGameroomDataMessage(self.client, self.player).sendWithLowID(self.plrData[i]["lowID"])
    	else:
    		try:
    			DataBase.leaveRoom(self, self.player.low_id)
    		except:
    			pass
    		self.player.err_code = 1
    		LoginFailedMessage(self.client, self.player, "Извини, сейчас нету доступных команд, но ты можешь создать свою!").send()