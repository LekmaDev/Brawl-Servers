from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import sqlite3 as sql
import json

class BrawlerLeader(Writer):

    def __init__(self, client, player, ID):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.conn = sql.connect("Database/leaders.db")
        self.cursor = self.conn.cursor()
        self.brawler = ID
    def by_tr(self,plr):
    	return json.loads(plr[2])['brawlersTrophies'][str(self.brawler)]
    def encode(self):
        self.indexOfPlayer = 1
        self.writeVint(0)
        self.writeVint(0)
        self.writeScId(16,self.brawler)
        self.writeString()
        fetch = DataBase.GetLeaderboardByBrawler(self, self.brawler)
        fetch.sort(key=self.by_tr, reverse=True)
        x=1
        y = 0
        self.writeVint(len(fetch))
        for i in fetch:
            	
            	self.writeVint(0) # High ID
            	self.writeVint(i[0]) # Low ID
            	self.writeVint(1)
            	self.writeVint(json.loads(i[2])['brawlersTrophies'][str(self.brawler)]) # Player Trophies
            	self.writeVint(1)
            	try:
            		DataBase.loadClub(self, i[5])
            		self.club = self.clubName
            	except:
            		self.club=""
            	self.writeString(self.club)
            	
            	self.writeString(i[1])# Player Name
            	self.writeVint(9999) # Player Level
            	self.writeVint(28000000 + i[3])
            	self.writeVint(43000000 + i[4])
            	if i[6]:
            		self.writeVint(i[4])
            	else:
            		self.writeVint(0)
            	self.writeVint(0) # Unknown


        self.writeVint(0)
        self.writeVint(x)
        self.writeVint(0)
        self.writeVint(0) # Leaderboard global TID
        self.writeString("RU")