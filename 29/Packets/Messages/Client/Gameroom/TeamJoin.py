from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Packets.Messages.Server.ServerError import ServerErrorMessage
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage

class TeamJoin(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        
    def decode(self):
    	#14358!!#
    	self.read_Vint()#type?
    	self.room_id = self.read_Vint()
    def process(self):
    	try:
    		DataBase.replaceValue(self, "roomID", self.room_id)
    		DataBase.getRoomAndJoin(self, self.token, self.player.room_id)
    		DataBase.loadGameroom(self)
    		if self.playerCount >= 3:
    			self.player.room_id = 0
    			DataBase.replaceValue(self, "roomID", 0)
    			DataBase.leaveRoom(self, self.player.low_id)
    			self.player.err_code=1
    			LoginFailedMessage(self.client, self.player, "Данная команда заполнена!").send()
    		else:
    			for i in self.plrData:
    				TeamGameroomDataMessage(self.client, self.player).sendWithLowID(self.plrData[i]["lowID"])
    	except:
    				TeamGameroomDataMessage(self.client, self.player).sendWithLowID(self.plrData[i]["lowID"])
    		