from Utils.Writer import Writer
from Utils.Fingerprint import Fingerprint
import random

class ServerErrorMessage(Writer):

    def __init__(self, client, player, ID):
        super().__init__(client)
        self.id = 24115
        self.player = player
        self.error = ID

    def encode(self):
        self.writeInt(self.error)