import random
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Logic.Boxes import Boxes
from Logic.Shop import *

from Utils.Writer import Writer

special1=random.choice([223, 224, 225, 226, 227, 295, 296, 297, 298, 299, 300, 301, 302, 314, 315, 316, 317, 318, 319, 320, 321, 334, 335, 336, 337, 338, 339, 340, 341, 346, 347, 348, 349, 350, 351, 352, 353])
special2=random.choice([223, 224, 225, 226, 227, 295, 296, 297, 298, 299, 300, 301, 302, 314, 315, 316, 317, 318, 319, 320, 321, 334, 335, 336, 337, 338, 339, 340, 341, 346, 347, 348, 349, 350, 351, 352, 353])
special3=random.choice([223, 224, 225, 226, 227, 295, 296, 297, 298, 299, 300, 301, 302, 314, 315, 316, 317, 318, 319, 320, 321, 334, 335, 336, 337, 338, 339, 340, 341, 346, 347, 348, 349, 350, 351, 352, 353])


class SkinsPinBox(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 25000
        self.player = player
        self.BoxData = Boxes.boxes

    def encode(self):
        # Box info
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)  # Multipler
        self.writeVint(100) # BoxID
        # Box info end

        # Pin 1
        self.writeVint(3)  #Reward Count
        self.writeVint(1) #Reward Amount
        self.writeVint(0) #CsvId 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, special1)# CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        #Pin 2
        self.writeVint(1) #Reward Amount
        self.writeVint(0) #CsvId 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, special2)# CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        #Pin 3
        self.writeVint(1) #Reward Amount
        self.writeVint(0) #CsvId 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, special3)# CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        
            

        # Box end
        for i in range(13):
            self.writeVint(0)
        