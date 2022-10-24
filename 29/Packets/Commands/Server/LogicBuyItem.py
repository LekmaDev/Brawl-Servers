import random
from Database.DatabaseManager import DataBase
from Utils.Writer import Writer
from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand
from Logic.Boxes import Boxes
from Logic.Shop import *



class LogicBuyItem(Writer):

    def __init__(self, client, player, id11, id22, id33, mult11, mult22, mult33, brawler11, brawler22, brawler33, skin11, skin22, skin33, pin1, pin2, pin3, accessory1, accessory2, accessory3):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.client = client
        self.BoxData = Boxes.boxes
        self.id1 = id11
        self.id2 = id22
        self.id3 = id33
        self.mult1 = mult11
        self.mult2 = mult22
        self.mult3 = mult33
        self.brawler1 = brawler11
        self.brawler2 = brawler22
        self.brawler3 = brawler33
        self.skin1 = skin11
        self.skin2 = skin22
        self.skin3 = skin33
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.accessory1 = accessory1
        self.accessory2 = accessory2
        self.accessory3 = accessory3

    def encode(self):
        #box header start
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(100)
        #box header end
        
        #reward info start

        if self.id1 != 0 and self.id2 != 0 and self.id3 != 0:
            self.writeVint(3) # Reward count
        elif self.id1 != 0 and self.id2 != 0:
            self.writeVint(2) # Reward count
        else:
            self.writeVint(1) # Reward count
        
        #reward 1

        if self.id1 == 1:
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id1 == 2: # Gems
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id1 == 3: # Star Powers
        	self.writeVint(1) # Reward Count
        	self.writeVint(1) # Value
        	self.writeVint(0) # ScId 16
        	self.writeVint(4) # Reward ID
        	self.writeVint(0) # ScId 29
        	self.writeVint(0) # ScId 52
        	self.writeScId(23, self.accessory1) # ScId 23
        	self.writeVint(0)
        elif self.id1 == 4: # Token Doubler
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(2) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id1 == 5: # Power points
            self.writeVint(self.mult1) # Reward amount
            self.writeScId(16, self.brawler1) # BrawlerID
            self.writeVint(6) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id1 == 6: # Brawler
            self.writeVint(self.mult1) # Reward amount
            self.writeScId(16, self.brawler1) # BrawlerID
            self.writeVint(1) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id1 == 7: # Skin
            self.writeVint(self.mult1)
            self.writeVint(0)
            self.writeVint(9)
            self.writeScId(29, self.skin1)
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) 
        elif self.id1 == 8: # Brawler Pin
        	self.writeVint(1)  #Reward Count
        	self.writeVint(1) #Reward Amount
        	self.writeVint(0) #CsvId 16
        	self.writeVint(11) # Reward ID
        	self.writeVint(0) # CsvID 29
        	self.writeScId(52, self.pin1)# CsvID 52
        	self.writeVint(0) # CsvID 23
        	self.writeVint(0)    	


        #reward 2
        if self.id2 == 1: # Gold
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id2 == 2: # Gems
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id2 == 3: # Star Powers
        	self.writeVint(1) # Reward Count
        	self.writeVint(1) # Value
        	self.writeVint(0) # ScId 16
        	self.writeVint(4) # Reward ID
        	self.writeVint(0) # ScId 29
        	self.writeVint(0) # ScId 52
        	self.writeScId(23, self.accessory2) # ScId 23
        	self.writeVint(0)    
        elif self.id2 == 4: # Token Doubler
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(2) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id2 == 5: # Power points
            self.writeVint(self.mult2) # Reward amount
            self.writeScId(16, self.brawler2) # BrawlerID
            self.writeVint(6) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id2 == 6: # Brawler
            self.writeVint(self.mult2) # Reward amount
            self.writeScId(16, self.brawler2) # BrawlerID
            self.writeVint(1) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id2 == 7: # Skin
            self.writeVint(self.mult2)
            self.writeVint(0)
            self.writeVint(9)
            self.writeScId(29, self.skin2)
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id2 == 8: # Brawler Pin
        	self.writeVint(1)  #Reward Count
        	self.writeVint(1) #Reward Amount
        	self.writeVint(0) #CsvId 16
        	self.writeVint(11) # Reward ID
        	self.writeVint(0) # CsvID 29
        	self.writeScId(52, self.pin2)# CsvID 52
        	self.writeVint(0) # CsvID 23
        	self.writeVint(0)
        	      	

        #reward 3
        if self.id3 == 1: # Gold
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id3 == 2: # Gems
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id3 == 3: # Star Powers
        	self.writeVint(1) # Reward Count
        	self.writeVint(1) # Value
        	self.writeVint(0) # ScId 16
        	self.writeVint(4) # Reward ID
        	self.writeVint(0) # ScId 29
        	self.writeVint(0) # ScId 52
        	self.writeScId(23, self.accessory3) # ScId 23
        	self.writeVint(0)                
        elif self.id3 == 4: # Token Doubler
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(2) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id3 == 5: # Power points
            self.writeVint(self.mult3) # Reward amount
            self.writeScId(16, self.brawler3) # BrawlerID
            self.writeVint(6) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id3 == 6: # Brawler
            self.writeVint(self.mult3) # Reward amount
            self.writeScId(16, self.brawler3) # BrawlerID
            self.writeVint(1) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id3 == 7: # Skin
            self.writeVint(self.mult3)
            self.writeVint(0) # CsvID 16
            self.writeVint(9)
            self.writeScId(29, self.skin3) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0)
        elif self.id3 == 8: # Brawler Pin
        	self.writeVint(1)  #Reward Count
        	self.writeVint(1) #Reward Amount
        	self.writeVint(0) #CsvId 16
        	self.writeVint(11) # Reward ID
        	self.writeVint(0) # CsvID 29
        	self.writeScId(52, self.pin3)# CsvID 52
        	self.writeVint(0) # CsvID 23
        	self.writeVint(0)          	            


        #reward info end
        for i in range(13):
            self.writeVint(0)