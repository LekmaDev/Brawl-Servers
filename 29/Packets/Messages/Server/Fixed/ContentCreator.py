from Utils.Writer import Writer
class SetContentCreatorServerMsg(Writer):
    def __init__(self, client, player, xxx):
        super().__init__(client)
        self.player = player
        self.id = 24111
        self.xxx = xxx
        self.client = client
    def encode(self):
    	self.writeVint(215)
    	self.writeVint(1)
    	self.writeString(self.xxx)
    	self.writeVint(1)