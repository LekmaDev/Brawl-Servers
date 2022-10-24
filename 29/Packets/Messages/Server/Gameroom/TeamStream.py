from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Utils.Writer import Writer
import random

class TeamStream(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 24131

    def encode(self):
        fm = []
        self.writeVint(0)#High ID
        self.writeVint(self.player.room_id)# Room ID
        self.writeVint(1)
        for i in range(1):
                if self.player.pin in fm:
                	self.writeVint(self.player.mode)
                else:
                	self.writeVint(8)
                # StreamEntry::encode
                self.writeVint(1)
                self.writeVint(self.player.ctick) # tick
                self.writeVint(0)
# High ID
                self.writeVint(self.player.low_id) # Low ID
                self.writeString(self.player.name)
                self.writeVint(1)
                self.writeVint(3600) # Age Seconds (TID_STREAM_ENTRY_AGE)
                self.writeVint(0) # Boolean
                if  not self.player.pin:
                	self.writeScId(40, random.randint(0, 11))
                else:
                	self.writeScId(40, self.player.pin) # Message Data ID (40 - messages.csv)
                	self.writeBoolean(True) # Target Boolean
                	self.writeString(self.player.name) # Target Name
                	self.writeVint(1) # ??
                	self.writeVint(52000319 + self.player.pin) # ScID (eg. 52000319 [trixie colette thanks pin] if message data id is (40, 46) and event 8)

        TeamGameroomDataMessage(self.client, self.player).send()

                

        