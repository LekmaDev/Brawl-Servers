from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import sqlite3 as sql

class GetLeaderboardLocalOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.conn = sql.connect("Database/leaders.db")
        self.cursor = self.conn.cursor()

    def encode(self):
        self.indexOfPlayer = 1
        self.writeBoolean(True)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("RU")
        fetch = DataBase.getLeaders(self)
        x=1
        self.writeVint(len(fetch))
        for i in fetch:
            	if i[0]==self.player.low_id:
            		x = fetch.index(i)+1
            	self.writeVint(0) # High ID
            	self.writeVint(i[0]) # Low ID
            	self.writeVint(1)
            	self.writeVint(i[2]) # Player Trophies
            	self.writeVint(1)
            	if i[6] != 0:
            		DataBase.loadClub(self, i[6])
            		self.club = self.clubName
            	else:
            		self.club=""
            	self.writeString(self.club)
            	
            	self.writeString(i[1])# Player Name
            	self.writeVint(9999) # Player Level
            	self.writeVint(28000000 + i[3])
            	self.writeVint(43000000 + i[4])
            	if i[5]:
            		self.writeVint(i[4])
            	else:
            		self.writeVint(0)
            	self.writeVint(0) # Unknown


        self.writeVint(0)
        self.writeVint(x)
        self.writeVint(0)
        self.writeVint(0) # Leaderboard global TID
        self.writeString("RU")