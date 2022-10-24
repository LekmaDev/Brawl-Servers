from random import *
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Logic.Boxes import Boxes

from Utils.Writer import Writer
class PinPackData(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(100)

        self.writeVint(5)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(11)
        self.writeVint(0)
        self.writeScId(52, randint(0, 318))
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(11)
        self.writeVint(0)
        self.writeScId(52, randint(0, 318))
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(11)
        self.writeVint(0)
        self.writeScId(52, randint(0, 318))
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(11)
        self.writeVint(0)
        self.writeScId(52, randint(0, 318))
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(11)
        self.writeVint(0)
        self.writeScId(52, randint(0, 318))
        self.writeVint(0)
        self.writeVint(0)

        for i in range(13):
            self.writeVint(0)