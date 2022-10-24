from Utils.Writer import Writer
class Friends(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.player = player
    def encode(self):
    	self.writeVint(1)