from Utils.Writer import Writer
import json


class AllianceMailWindow(Writer):

    def __init__(self, client, player, data):
        super().__init__(client)
        self.id = 24333
        self.player = player
        self.data = data

    def encode(self):
        self.writeVint(self.data) # Event type