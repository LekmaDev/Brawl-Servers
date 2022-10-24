from random import *
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Logic.Boxes import Boxes
from Logic.Shop import Shop

from Utils.Writer import Writer
class ShopResponse(Writer):
	def __init__(self, client, player,data,var,count):
	       super().__init__(client)
	       self.id = 24111
	       self.player = player
	       self.var = var
	       self.count = count
	       self.data= data
	       
	def encode(self):
	       self.writeVint(203) # CommandID
	       self.writeVint(0)   # Unknown
	       self.writeVint(1)   # Unknown
	       self.writeVint(100)  # BoxID
	       self.writeVint(1) # Reward count
	       self.writeVint(self.count) # Reward amount
	       DataBase.replaceValue(self, self.data["name"], self.var)
	       if self.data["id"] == 6:
	       	self.writeScId(16, self.data["scid"]) # CsvI
	       else:
	       	self.writeVint(0)
	       DataBase.replaceValue(self, self.data["name"], self.var)
	       self.writeVint(self.data["id"])                           # Reward
	       if self.data["id"] == 9:
	       	self.writeScId(29, self.data["skin"])#skin
	       else:
	       	self.writeVint(0)
	       if self.data['id'] == 11:
	          self.writeScId(52, self.data["pin"]) # 52 csv ID
	       else:
	       	self.writeVint(0)
	       if self.data['id'] == 4:
	          self.writeScId(23, self.data["StarPowerUnlocked"]) # 52 csv ID
	       else:
	       	self.writeVint(0)
	       self.writeVint(0)
	       for i in range(13):
	       	self.writeVint(0)
	       