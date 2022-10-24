from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
import random


class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0


    def encode(self, fields, player):
        # ПОДПИСЫВАЙСЯ НА t.me/leakarfiv
        self.writeVInt(0)#room state
        self.writeBoolean(False)#??
        self.writeVInt(0)#??

        self.writeLong(0, 1)#room id
        self.writeVInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)#??
        self.writeVInt(0)
        self.writeVInt(0)#??
        self.writeVInt(0)
        self.writeDataReference(15, 7)#map

        self.writeBoolean(False)#battleplayermap?

        self.writeVInt(1)#i guess 1 - someone 0 - no one
        for x in range(1):
            self.writeBoolean(True)#isowner
            self.writeLong(player.ID[0], player.ID[1])#id
            self.writeDataReference(16, player.SelectedBrawlers[0])#brawler
            self.writeDataReference(0, 0)#brawler skin?
            self.writeVInt(0)#??
            self.writeVInt(0)#brawler trophy
            self.writeVInt(0)#??
            self.writeVInt(1)#level
            self.writeVInt(3)#state (3 - true)
            self.writeBoolean(False)#ready False - no True - yes
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            #playerdisplaydata
            self.writeString(player.Name)
            self.writeVInt(100)#exp
            self.writeVInt(28000000 + player.Thumbnail)#icon
            self.writeVInt(43000000 + player.Namecolor)#name color
            self.writeVInt(-1)#?? (with -1 work)
            self.writeDataReference(0, 0)
            self.writeDataReference(0, 0)
            self.writeDataReference(0, 0)#sp?
            self.writeDataReference(0, 0)
            self.writeVInt(0)
            self.writeVInt(0)
            #playerdisplaydata end

            self.writeVInt(0)#invite player array
	    # ПОДПИСЫВАЙСЯ НА t.me/leakarfiv

    def decode(self):
        fields = {}
        fields["TeamID"] = self.readVLong()
        fields["MessageCount"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24124, fields, calling_instance.player)

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion