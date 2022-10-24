from Utils.Writer import Writer


class TeamChatMsg(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24131
        self.player = player
    def encode(self):
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(1)#count
        self.writeVint(0)
        self.writeVint(self.player.low_id)#lowid
        self.writeString(self.player.name)#name
        self.writeVint(3)#rolw
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("Test9339")#msg