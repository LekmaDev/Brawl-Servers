from random import *
from Database.DatabaseManager import DataBase

from Utils.Writer import Writer

import random,datetime


class LogicAddNotificationCommand(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.msg = msg

    def encode(self):
        self.writeVint(206)
        DataBase.loadClub(self, self.player.club_low_id)
        print(self.notifData)
        if len(self.notifData)>0:
        	self.writeVint(1)  # Массив сообщени
        	if True:
        		if 1==1:
        			self.writeVint(82) #ID #81
        			self.writeInt(0) #
        			self.writeByte(0) #вроде статус прочтанный
        			self.writeInt(0)#Таймер
        			self.writeString(self.msg) #сообщение
        			DataBase.GetMemberData(self, self.player.low_id)
        			self.writeString(self.plrname) #автор сообщения
        			self.writeVint(43000000+self.plrnamecolor)
        			self.writeVint(28000000) #Иконк
        			self.writeVint(43000000+self.plrnamecolor)