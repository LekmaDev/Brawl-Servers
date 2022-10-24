from Utils.Writer import Writer
import random


class AllianceWarMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24776
        self.player = player

    def encode(self):
        self.writeInt(0) # High ID
        self.writeInt(1) # Low ID

        self.writeVint(0)

        # AllianceWarNode
        maps = [7]
        self.writeVint(len(maps))
        for x in maps:
            self.writeVint(0)
            self.writeVint(maps.index(x) + 1) # Horizontal Position
            self.writeVint(0)  # Vertical Position
            self.writeVint(random.randint(1, 4))# SpriteID
            self.writeScId(15, x)         # MapID
            self.writeVint(maps.index(x)) # Node State
            self.writeVint(50)            # Timer
            self.writeVint(0)             # Star Number

            self.writeVint(0) # array
            for x in range(0):
                self.writeVint(x)

        # AllianceWarFaction
        self.writeVint(1)
        for x in range(1):
            self.writeVint(random.randint(1, 4)) # SpriteID
            self.writeVint(x)
