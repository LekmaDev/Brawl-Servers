from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase

class TeamBrawler(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        print(initial_bytes)
    def decode(self):
    	#14369!#
    	self.read_Vint()#40?
    	self.read_int()
    	data=[]
    	for i in range(2):
    		data.append(self.read_int())
    	print(data)
#b'(\x00\x01\x00\x00\x00\x009@"R\x00\x88\x90\xa1\x0f\x00'
    def process(self):
    	pass