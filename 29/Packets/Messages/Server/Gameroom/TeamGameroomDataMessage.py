from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import sqlite3 as sql

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player, roomType=1):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.playerCount = 0
        self.conn = sql.connect("Database/leaders.db")
        self.cursor = self.conn.cursor()
        self.roomType = roomType

    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        if self.player.Brawler_starPower[str(self.player.brawler_id)] >= 1:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 2
        else:
            brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        DataBase.loadGameroom(self)
        if self.player.room_id != 0:
            try:
            	self.writeVint(self.roomType)
            except:
            	if len(self.plrData)>1:
            		self.writeVint(0)
            	else:
            		self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
        
            self.writeInt(0)
            self.writeInt(self.player.room_id)

            self.writeVint(1594036200)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            self.writeScId(15, self.player.map_id)               # MapID

            for plr in self.plrData.values():
                # Player
                self.writeVint(self.playerCount)
                self.writeVint(plr['host'])       # Gameroom owner boolean
                self.writeInt(0)                                      # HighID
                self.writeInt(int(plr["lowID"]))         # LowID

                self.writeScId(16, plr["brawlerID"])             # BrawlerID
                self.writeScId(29, plr["skinID"])
                self.writeVint(brawler_trophies)
                self.writeVint(brawler_trophies_for_rank)
                self.writeVint(brawler_level)

                self.writeVint(plr["status"])                              # Player State | 11: Events, 10: Brawlers, 9: Writing..., 8: Training, 7: Spectactor, 6: Offline, 5: End Combat Screen, 4: Searching, 3: Not Ready, 2: AFK, 1: In Combat, 0: OffLine
                self.writeVint(plr["Ready"])    # Is ready
                self.writeVint(plr["Team"])     # Team | 0: Blue, 1: Red
                self.writeVint(6)
                self.writeVint(2)

                self.writeString(plr["name"])                  # Player name
                self.writeVint(0)
                self.writeVint(28000000 + plr["profileIcon"])  # Player icon
                self.writeVint(43000000 + plr["namecolor"])    # Player name color
                self.writeVint(0)#Invite array!
                
                if self.useGadget:
                    self.writeScId(23, plr["starpower"])       # Starpower
                    self.writeScId(23, plr["gadget"])          # Gadget
                else:
                    self.writeScId(23, plr["starpower"])       # Starpower
                    self.writeScId(0, 0)                                            # Gadget

            self.writeVint(0)
            self.writeVint(0)#invite array again
            self.writeVint(0)#bots array
            self.writeVint(0)
            self.writeVint(6)
            DataBase.replaceValue(self, "online", 1)

        else:
            print(self.player.room_id)
