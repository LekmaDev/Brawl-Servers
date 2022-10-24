from Packets.Messages.Server.Alliance.AllianceMemberEntryMessage import AllianceMemberEntryMessage
from Packets.Messages.Server.Alliance.My_Alliance_Message import MyAllianceMessage
from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Server.Alliance.Events.AllianceJoinOkMessage import AllianceJoinOkMessage
from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage
from Packets.Messages.Server.Alliance.Events.JoinFail import AllianceJoinFail

from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader


class Join_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.club_high_id = self.read_int()
        self.clubID = self.read_int()

    def process(self):
        DataBase.loadClub(self, self.clubID)
        if self.clubmembercount == 100:
        	AllianceJoinFail(self.client, self.player).send()
        	return
        self.player.club_low_id = self.clubID
        self.player.club_role = 1
        DataBase.replaceValue(self, 'clubRole', 1)
        DataBase.replaceValue(self, 'clubID', self.player.club_low_id)

        # Member adding
        DataBase.AddMember(self, self.player.club_low_id, self.player.low_id, self.player.name, 1)
        DataBase.Addmsg(self, self.player.club_low_id, 4, 0, self.player.low_id, self.player.name, self.player.club_role, 3)

        # Info
        AllianceJoinOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, self.player.club_low_id).send()
        AllianceStreamMessage(self.client, self.player, self.player.club_low_id, 0).send()
        DataBase.loadClub(self, self.player.club_low_id)
        for i in self.plrids:
            AllianceChatServerMessage(self.client, self.player, 3, self.player.club_low_id).sendWithLowID(i)
        #AllianceMemberEntryMessage(self.client, self.player).sendToOthers()