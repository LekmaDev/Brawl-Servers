from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import random
import time

class LobbyInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeString("-------------\n    NanoBrawl\n-------------\nОжидайте скины!")

        self.writeVint(1) # array
        for x in range(0):
            self.writeVint(1)
            self.writeVint(1)
            self.writeVint(1)
            self.writeVint(1)
            self.writeVint(1)
