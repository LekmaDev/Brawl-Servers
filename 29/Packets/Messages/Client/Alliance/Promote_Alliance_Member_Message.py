from Packets.Messages.Server.Alliance.Events.AllianceRoleChangedOKMessage import AllianceRoleChangedOKMessage

from Packets.Messages.Server.Alliance.My_Alliance_Message import MyAllianceMessage

from Utils.Helpers import Helpers
from Database.DatabaseManager import DataBase
from random import choice
from string import ascii_uppercase
import json

from Utils.Reader import BSMessageReader


class Promote_Alliance_Member_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.TargetHighID = self.read_int()
        self.TargetLowID = self.read_int()
        self.TargetedRole = self.read_Vint()

    def process(self):

        # Replacing value
        
        
        # Sending confirmation and updated data
        account = DataBase.loadbyID(self, self.TargetLowID)
        role = account[9]
        if self.player.club_role in [0, 1]:
        	return
        if self.TargetedRole > role:
        	AllianceRoleChangedOKMessage(self.client, self.player, 0).send()
        else:
        	AllianceRoleChangedOKMessage(self.client, self.player, 1).send()
        DataBase.replaceOtherValue(self, self.TargetLowID, 'clubRole', self.TargetedRole)
        account = DataBase.loadbyID(self, self.TargetLowID)
        if self.player.club_role == 2 and account[9] ==2:
              	DataBase.replaceValue(self, "clubRole", 4)
    		        	
        MyAllianceMessage(self.client, self.player, self.player.club_low_id).send()