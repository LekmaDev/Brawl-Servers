from Utils.Writer import Writer


class TeamInviteMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 14365
        self.player = player
        
    def encode(self):
        self.writeInt(0) # High ID Room
        self.writeInt(1) # Low ID Room
        
        #Player Data Entry
        self.writeInt(0) # High ID Player
        self.writeInt(1) # Low ID Player
        self.writeString("Name") # NickName Player
        self.writeVint(1) # ?
        self.writeVint(1) # Slot