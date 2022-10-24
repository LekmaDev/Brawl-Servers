from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Cards import Cards

from Utils.Reader import BSMessageReader


class TeamChangeMemberSettingsMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.csv_id = self.read_Vint()
        if self.csv_id == 23:
            self.StarpowerID = self.read_Vint()
        else:
            self.csv_id = self.read_Vint()
            self.BrawlerSkinId = self.read_Vint()

    def process(self):
        if self.csv_id == 29:
            self.player.brawler_id = Characters.get_brawler_by_skin_id(self, self.BrawlerSkinId)
            self.player.starpower = Cards.get_spg_by_brawler_id(self, self.player.brawler_id, 4)
            self.player.gadget = Cards.get_spg_by_brawler_id(self, self.player.brawler_id, 5)
        else:
            try:
            	self.player.starpower = self.StarpowerID
            except:
            	pass
            self.player.gadget = Cards.get_spg_by_brawler_id(self, self.player.brawler_id, 5)
        
        DataBase.replaceValue(self, 'starpower', self.player.starpower)
        DataBase.replaceValue(self, 'gadget', self.player.gadget)
        try:
        	self.player.skin_id = self.BrawlerSkinId
        except:
        	pass
        DataBase.replaceValue(self, "skinID", self.player.skin_id)
        DataBase.UpdateGameroomPlayerInfo(self, self.player.low_id)
        DataBase.loadGameroom(self)
        for i in self.plrData:
        	TeamGameroomDataMessage(self.client, self.player).sendWithLowID(i)