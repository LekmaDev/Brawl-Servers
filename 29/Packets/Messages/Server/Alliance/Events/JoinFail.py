from Utils.Writer import Writer
import json


class AllianceJoinFail(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24333
        self.player = player

    def encode(self):
        self.writeVint(42) # Event type