from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage
from Packets.Messages.Server.AllianceBot.Alliance_Bot_Chat_Server_Message import AllianceBotChatServerMessage
from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
import time
from Packets.Messages.Server.Alliance.My_Alliance_Message import MyAllianceMessage
from Packets.Messages.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader
import tracemalloc
import json
import sqlite3 as sql
import base64, datetime
from Database.sqlDB import VIPDB
tracemalloc.start()
class AllianceChatMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False
    def decode(self):
        self.msg = self.read_string()
        self.args = self.msg.strip().split()
        self.command=self.args[0]
        if self.command == "/theme":
        	self.IsAcmd=True
        	if self.player.vip:
        		if len(self.args)==2:
        			self.args[1] = int(self.args[1])
        			if self.args[1] > -1 and self.args[1] < 26 and self.args[1] != 5:
        				DataBase.replaceValue(self, 'theme', self.args[1])
        				self.send_ofs=True
        			else:
        				self.bot_msg="Указанного фона не существует!"
        		else:
        			self.bot_msg="Укажите айди темы!\nВсе доступные темы:\n0 - Дефолт тема\n1 - LNY\n2 -  Golden Week (фон с собаками)\n3 - Ретрополис\n4 - Меха\n6 - Фон с пиратами\n7 - LNY20 (Аркадное обновление)\n8 - PSG\n9 - SC10 (10 лет supercell)\n10 - Базар тары\n11 - Суперсити\n12 - Старр парк\n13 - Лунный фестиваль\n14 - Мировой финал 2020\n15 - Хэллоуин 2020\n16 - Зимний фон (Веселые каникулы)\n17 - Зимний фон (с партиклами)\n18 - Коспоопера старр\n19 - LNY21\n20 - ActionShow\n21 - Ramadan\n22 - Дефолт тема\n23 - Пляж\n24 - Punk\n25 - [Custom]"
        	else:
        		self.bot_msg = "У вас нет VIP!"
        elif self.command == "/set":
        	self.IsAcmd=True
        	adminauth = self.args[1]
        	toset = self.args[2]
        	value = self.args[3]
        	try:
        		decr = "zl1OPD3V"
        	except:
        		self.bot_msg="Ошибка декодировки ключа!"
        	timestamp = 0
        	whoget = self.player.low_id
        	if decr != self.args[1]:
        		self.bot_msg="Ключ был выдам не вам!"
        		return 0
        	if toset == "trophies":
        		f = open("config.json", "r")
        		data = json.loads(f.read())
        		try:
        			data["TrophiesForPlrs"]=int(value)
        			json.dump(data, open("config.json", "w"))
        			self.bot_msg=f"OK! Ключ был выдан: {whoget} ID\nКлюч был создан: {datetime.datetime.timestamp(datetime.datetime.now())-timestamp} секунд назад"
        		except Exception as e:
        			self.bot_msg=f"Error: {e}"
        	elif toset == "vip":
        		DataBase.replaceOtherValue(self, int(value), 'vip', 1)
        		self.bot_msg="ok"
        	elif toset == "sqlreq":
        		DataBase.callbackSQLQ(self, ' '.join(self.args[3:]))
        		self.bot_msg="OK"
        	elif toset == "theme":
        		try:
        			DataBase.set2All(self, 'theme', int(value))
        			self.bot_msg=f"OK! Ключ был выдан: {whoget} ID\nКлюч был создан: {datetime.datetime.timestamp(datetime.datetime.now())-timestamp} секунд назад"
        		except Exception as e:
        			self.bot_msg=f"Error: {e}"
        	else:
        		self.bot_msg="Unkown param"
        elif self.command == "/help":
        		self.IsAcmd=True
        		self.bot_msg=f"Команды:\n==Для обычных игроков==\n/info - информация о вашем аккаунте\n/clubname [имя] - изменить имя клуба\n===VIP===\n/theme [ID] - сменить фон"
        elif self.command=="/info":
        	self.IsAcmd=True
        	self.bot_msg=f"STARR PREMIUM™: {self.player.vip}\n\n\nТВОЙ ПРОФИЛЬ:\nТРОФЕИ: {self.player.trophies}\nНИК: {self.player.name}\nLOW ID: {self.player.low_id}\nТОКЕН: {self.player.token}\nЗАПОМНИ!\nНИКОМУ НЕ СООБЩАЙ ТОКЕН!"
        
    def process(self):
        
        if self.send_ofs == False and self.IsAcmd == False:
            DataBase.Addmsg(self, self.player.club_low_id, 2, 0, self.player.low_id, self.player.name, self.player.club_role, self.msg)
            DataBase.loadClub(self, self.player.club_low_id)
            for i in self.plrids:
                AllianceChatServerMessage(self.client, self.player, self.msg, self.player.club_low_id).sendWithLowID(i)
                #AllianceStreamMessage(self.client, self.player, self.player.club_low_id, 0).send()

        if self.bot_msg != '':
            AllianceChatServerMessage(self.client, self.player, self.msg, self.player.club_low_id, True).send()
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send()

        if self.send_ofs:
            LoginFailedMessage(self.client, self.player, 'Для сохранения изменений вам нужно перезайти!').send()