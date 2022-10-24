from Packets.Messages.Server.Leaderboard.TopGlobalPlayersDataMessage import GetLeaderboardGlobalOkMessage
from Packets.Messages.Server.Leaderboard.TopLocalPlayersDataMessage import GetLeaderboardLocalOkMessage
from Packets.Messages.Server.Leaderboard.TopGlobalClubsDataMessage import GetLeaderboardClubGlobalOkMessage
from Packets.Messages.Server.Leaderboard.TopLocalClubsDataMessage import GetLeaderboardClubLocalOkMessage
from Packets.Messages.Server.Leaderboard.Brawler import BrawlerLeader
from Database.DatabaseManager import DataBase

import sqlite3 as sql
from Utils.Reader import BSMessageReader



class GetLeaderboardMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.conn = sql.connect("Database/leaders.db")
        self.cursor = self.conn.cursor()
        

    def decode(self):
        self.is_local = self.read_Vint()
        self.type = self.read_Vint()
        self.read_Vint()


    def process(self):
        if self.type==1:
        	if self.is_local:
        		GetLeaderboardLocalOkMessage(self.client, self.player).send()
        	else:
        		GetLeaderboardGlobalOkMessage(self.client, self.player).send()
        elif self.type==2:
        	BrawlerLeader(self.client, self.player, self.read_Vint()).send()
        else:
        	BrawlerLeader(self.client, self.player, self.read_Vint()).send()