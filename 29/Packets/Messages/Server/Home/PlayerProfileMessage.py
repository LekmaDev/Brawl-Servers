from os import truncate
import json
from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, high_id, low_id, players):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.high_id = high_id
        self.low_id = low_id
        self.players = players

    def encode(self):
            player = self.players

            self.writeVint(self.high_id)  # High ID
            self.writeVint(self.low_id)  # Low Id
            self.writeVint(0)  # Unknown

            self.writeVint(39)  # Brawlers array
            brawlerData = json.loads(player[33])
            for brawler_id in brawlerData["brawlersTrophies"]:
                    if brawler_id != 33:
                    	self.writeScId(16, int(brawler_id))
                    	self.writeVint(0)
                    	self.writeVint(brawlerData["brawlersTrophies"][brawler_id])  # Trophies
                    	self.writeVint(brawlerData["brawlersTrophiesForRank"][brawler_id])
                    	self.writeVint(brawlerData["brawlerPowerLevel"][brawler_id])
                    else:
                    	self.writeScId(16, 33)
                    	self.writeVint(0)
                    	self.writeVint(0)
                    	self.writeVint(0)
                    	self.writeVint(0)
            self.writeVint(14)
            self.writeVint(1)
            self.writeVint(player[15])  # 3v3 victories

            self.writeVint(2)
            self.writeVint(player[11]) # Player experience

            self.writeVint(3)
            self.writeVint(player[23]) # Trophies

            self.writeVint(4)
            self.writeVint(brawlerData['highest_trophies'])  # Highest trophies

            self.writeVint(5)
            self.writeVint(39) # Brawlers list
                
            self.writeVint(7)
            self.writeVint(28000000 + player[25]) # Profile icon??

            self.writeVint(8)
            self.writeVint(player[13])  # Solo victories

            self.writeVint(9)
            self.writeVint(0) # Best robo rumble time

            self.writeVint(10)
            self.writeVint(0) # Best time as big brawler

            self.writeVint(11)
            self.writeVint(player[14])  # Duo victories
                
            self.writeVint(12)
            self.writeVint(0) # Highest boss fight lvl passed

            self.writeVint(13)
            self.writeVint(0) # Highest power player points 

            self.writeVint(14)
            self.writeVint(0) # Highest power play rank

            self.writeVint(15)
            self.writeVint(brawlerData['chwins'])  # most challenge wins

            self.writeString(player[2])#name
            self.writeVint(player[11])
            self.writeVint(28000000 + player[25])  # Profile icon
            self.writeVint(43000000 + player[26])  # Name color
            if player[5]:
            	self.writeVint(player[26])
            else:
            	self.writeVint(0)

            if player[6] != 0:
                    DataBase.loadClub(self, player[6])

                    self.writeBoolean(True)  # Is in club

                    self.writeInt(0)
                    self.writeInt(player[6])
                    self.writeString(self.clubName)  # club name
                    self.writeVint(8)
                    self.writeVint(self.clubbadgeID)  # Club badgeID
                    self.writeVint(self.clubtype)  # club type | 1 = Open, 2 = invite only, 3 = closed
                    self.writeVint(self.clubmembercount)  # Current members count
                    self.writeVint(self.clubtrophies)
                    self.writeVint(self.clubtrophiesneeded)  # Trophy required
                    self.writeVint(0)  # (Unknown)
                    self.writeString(self.clubregion)  # region
                    self.writeVint(0)  # (Unknown)
                    self.writeVint(0) # (Unknown)
                    self.writeVint(25)
                    self.writeVint(player[9])
            else:
                    self.writeBoolean(False)
                    self.writeVint(0)
