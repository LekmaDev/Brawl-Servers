#10501
from Utils.ByteStream import Reader
class AcceptFriendMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        self.readInt() # High ID
        self.readInt() # Low ID
    def process(self):
        pass