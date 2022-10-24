from Packets.Messages.Server.Alliance.Alliance_Data_Message import AllianceDataMessage
from Packets.Messages.Server.Alliance.Events.Mail import AllianceMailWindow
from Packets.Messages.Server.NotifAdd import LogicAddNotificationCommand
from Utils.Reader import BSMessageReader
from Database.DatabaseManager import DataBase
class SendClubMail(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        print(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
    	self.read_int()
    	self.msg = self.read_string()
    def process(self):
        if self.msg:
        	DataBase.setNotifData(self, self.msg, self.player.low_id)
        	AllianceMailWindow(self.client, self.player, 113).send()
        	DataBase.loadClub(self, self.player.club_low_id)
        	for i in self.plrids:
        		LogicAddNotificationCommand(self.client, self.player, self.msg).sendWithLowID(i)
        else:
        	AllianceMailWindow(self.client, self.player, 114).send()
        #AllianceDataMessage(self.client, self.player, self.clubHighID, self.clubLowID).send()