from Database.DatabaseManager import DataBase
from Packets.Messages.Server.Gameroom.TeamLeftMessage import TeamLeftMessage
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Utils.Reader import BSMessageReader


class TeamLeaveMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        DataBase.loadGameroom(self)
        data = self.plrData
        for i in data:
        	if data[i]["host"] == 1:
        		DataBase.replaceOtherValue(self, data[i]["lowID"], "roomID", 0)
        		TeamLeftMessage(self.client, self.player).sendWithLowID(data[i]["lowID"])
        		DataBase.replaceValue(self, 'roomID', 0)
        		self.player.room_id = 0
        		if i == len(data)-1:
        			DataBase.removeRoom(self)
        	else:
        		DataBase.leaveRoom(self, self.player.low_id)
        		DataBase.replaceValue(self, 'roomID', 0)
        		self.player.room_id = 0
        		TeamLeftMessage(self.client, self.player).send()
        		for i in data:
        			if data[i]["lowID"]!=self.player.low_id:
        				TeamGameroomDataMessage(self.client, self.player).sendWithLowID(data[i]["lowID"])
#        	if data[i]["host"] == 1:
#        		DataBase.leaveFromRoom(self, self.player.low_id)
#        		DataBase.removeRoom(self)
#        	else:
#        		DataBase.leaveFromRoom(self, self.player.low_id)