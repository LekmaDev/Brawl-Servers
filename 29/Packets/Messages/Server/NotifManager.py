from Database.DatabaseManager import DataBase
import json
class NotifManager:
	def __init__(self, player, client):
		self.plr = player
	def getClubNotifications(self):
		DataBase.loadClub(self, self.plr.club_low_id)
		self.notifList=[]
		index=[]
		for i in self.notifData:
				index.append(i)
		for i in index[::-1]:
			if index[::-1].index(i)<=4:
				self.notifList.append(json.dumps(self.notifData[str(i)]))
		self.notifList.sort(reverse=False)
		return self.notifList
	def getSysNotifications(self):
		return
	def SeasonEnd(self):
		bslist = []
		for i in (self.plr.brawlers_trophies):
			if self.plr.brawlers_trophies[str(i)]>=501:
				bslist.append(i)
		result={}
		for i in bslist:
			result[i]={}
			result[i]["old"]=self.plr.brawlers_trophies[str(i)]
			n = 20
			if 525<self.plr.brawlers_trophies[str(i)]<551:
				n=50
			elif 551<self.plr.brawlers_trophies[str(i)]<575:
				n=70
			elif 575<self.plr.brawlers_trophies[str(i)]<600:
				n=80
			elif 600<self.plr.brawlers_trophies[str(i)]<624:
				n=90
			elif 624<self.plr.brawlers_trophies[str(i)]<650:
				n = 100
			elif 650<self.plr.brawlers_trophies[str(i)]<675:
				n = 110
			elif 675<self.plr.brawlers_trophies[str(i)]<700:
				n = 120
			elif 700<self.plr.brawlers_trophies[str(i)]<724:
				n=130
			elif 724<self.plr.brawlers_trophies[str(i)]<750:
				n = 140
			elif 750<self.plr.brawlers_trophies[str(i)]<775:
				n = 150
			elif 775<self.plr.brawlers_trophies[str(i)]<800:
				n = 160
			elif 800<self.plr.brawlers_trophies[str(i)]<824:
				n=170
			elif 824<self.plr.brawlers_trophies[str(i)]<850:
				n = 180
			elif 850<self.plr.brawlers_trophies[str(i)]<875:
				n = 190
			elif 875<self.plr.brawlers_trophies[str(i)]<900:
				n = 200
			elif 900<self.plr.brawlers_trophies[str(i)]<924:
				n=210
			elif 924<self.plr.brawlers_trophies[str(i)]<950:
				n = 220
			elif 950<self.plr.brawlers_trophies[str(i)]<975:
				n = 230
			elif 975<self.plr.brawlers_trophies[str(i)]<1000:
				n = 250
			elif self.plr.brawlers_trophies[str(i)]>=1000:
				n=400+(self.plr.brawlers_trophies[str(i)]-1000)//5
			self.player = self.plr
			self.player.star_points+=n
			DataBase.replaceValue(self, 'starpoints', self.player.star_points)
			result[i]["new"]=n
			result[i]["sp"]=n
			self.plr.brawlers_trophies[str(i)]-=n
			DataBase.replaceValue(self, 'brawlersTrophies', self.plr.brawlers_trophies)
		return result
	def getAllNotif(self):
		return NotifManager(self.plr, self.cl).getClubNotifications().append( f"Привет, {self.plr.name}! Обновление от 20.11.2021 уже тут!\nНововведения:\nКлубная почта")