from Utils.Reader import BSMessageReader
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.Alliance.Events.KickMemberOK import AllianceKickMemberOK
from Packets.Messages.Server.Alliance.My_Alliance_Message import MyAllianceMessage
from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage


class KickDudnick(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
    	self.read_int()
    	self.lowID = self.read_int()
    	self.reason = self.read_string()
    def process(self):
    	account = DataBase.loadbyID(self, self.lowID)
    	
    	DataBase.AddMember(self, account[6], self.lowID, account[2], 2)
    	AllianceKickMemberOK(self.client, self.player).send()
    	self.clubLowID = account[6]
    	i = DataBase.loadbyID(self, self.player.low_id)
    	
    	DataBase.replaceOtherValue(self, self.lowID, "clubID", 0)
    	DataBase.replaceOtherValue(self, self.lowID, "clubRole", 0)
    	DataBase.Addmsg(self, self.player.club_low_id, 4, 1, account[1], self.player.name, self.player.club_role, 1)
    	
    		
    	MyAllianceMessage(self.client, self.player, self.clubLowID).send()
    	DataBase.loadClub(self, self.player.club_low_id)
    	for i in self.plrids:
    		AllianceChatServerMessage(self.client, self.player, "dev", self.player.club_low_id).sendWithLowID(i)