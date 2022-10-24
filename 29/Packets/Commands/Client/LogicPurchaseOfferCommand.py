from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand
from Packets.Commands.Server.LogicBuyItem import LogicBuyItem
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Database.DatabaseManager import DataBase
from Logic.Shop import Shop

import random
import time
from Utils.Reader import BSMessageReader

class LogicPurchaseOfferCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.offer_index = self.read_Vint()
        self.BrawlerID = self.read_Vint()


    def process(self):
        Shop.loadOffers(self)
        offers = self.offers
        id1 = offers[self.offer_index]['ID'][0]
        id2 = offers[self.offer_index]['ID'][1]
        id3 = offers[self.offer_index]['ID'][2]
        multi1 = offers[self.offer_index]['Multiplier'][0]
        multi2 = offers[self.offer_index]['Multiplier'][1]
        multi3 = offers[self.offer_index]['Multiplier'][2]
        brawler1 = offers[self.offer_index]['BrawlerID'][0]
        brawler2 = offers[self.offer_index]['BrawlerID'][1]
        brawler3 = offers[self.offer_index]['BrawlerID'][2]
        skin1 = offers[self.offer_index]['SkinID'][0]
        skin2 = offers[self.offer_index]['SkinID'][1]
        skin3 = offers[self.offer_index]['SkinID'][2]
        accessory1 = offers[self.offer_index]['SkinID'][0]
        accessory2 = offers[self.offer_index]['SkinID'][1]
        accessory3 = offers[self.offer_index]['SkinID'][2]
        pin1 = offers[self.offer_index]['SkinID'][0]
        pin2 = offers[self.offer_index]['SkinID'][1]
        pin3 = offers[self.offer_index]['SkinID'][2]

        ID1 = 0
        ID2 = 0
        ID3 = 0

        if offers[self.offer_index]['ShopType'] == 0:
            self.player.gems = self.player.gems - offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gems', self.player.gems)
        elif offers[self.offer_index]['ShopType'] == 1:
            self.player.gold = self.player.gold - offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gold', self.player.gold)
        elif offers[self.offer_index]['ShopType'] == 2:
            self.player.gems = self.player.gems - offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gems', self.player.gems)                  
        elif offers[self.offer_index]['ShopType'] == 3:
            self.player.star_points = self.player.star_points - offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'starpoints', self.player.star_points)
 

        if id1 == 1:
            self.player.gold = self.player.gold + multi1
            DataBase.replaceValue(self, 'gold', self.player.gold)
            ID1 = 1
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 1:
            self.player.gold = self.player.gold + multi2
            DataBase.replaceValue(self, 'gold', self.player.gold)
            ID2 = 1
        if id3 == 1:
            self.player.gold = self.player.gold + multi3
            DataBase.replaceValue(self, 'gold', self.player.gold)
            ID3 = 1
            
        if id1 == 24:
            self.player.skins[str(skin1)]=1
            DataBase.replaceValue(self, 'skins', self.player.skins)
            ID1 = 7
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 24:
            self.player.skins[str(skin2)]=1
            DataBase.replaceValue(self, 'skins', self.player.skins)
            ID2 = 7
        if id3 == 24:
            self.player.skins[str(skin3)]=1
            DataBase.replaceValue(self, 'skins', self.player.skins)
            ID3 = 7            

        if id1 == 16:
            self.player.gems = self.player.gems + multi1
            DataBase.replaceValue(self, 'gems', self.player.gems)
            ID1 = 2
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 16:
            self.player.gems = self.player.gems + multi2
            DataBase.replaceValue(self, 'gems', self.player.gems)
            ID2 = 2
        if id3 == 16:
            self.player.gems = self.player.gems + multi3
            DataBase.replaceValue(self, 'gems', self.player.gems)
            ID3 = 2

        if id1 == 5:
        	self.player.skills[str(accessory1)]+=1
        	DataBase.replaceValue(self, 'skills', self.player.skills)
        	ID1 = 3
        	Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 5:
            self.player.skills[str(accessory2)]+=1
            DataBase.replaceValue(self, 'skills', self.player.skills)
            ID2 = 3
        if id3 == 5:
            self.player.skills[str(accessory3)]+=1
            DataBase.replaceValue(self, 'skills', self.player.skills)
            ID3 = 3
            
        if id1 == 19:
            self.player.emotes[str(pin1)]=1
            DataBase.replaceValue(self, 'emotes', self.player.emotes)
            ID1 = 8 
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 19:
            self.player.emotes[str(pin2)]=1
            DataBase.replaceValue(self, 'emotes', self.player.emotes)
            ID2 = 8 
        if id3 == 19:
            self.player.emotes[str(pin3)]=1
            DataBase.replaceValue(self, 'emotes', self.player.emotes)
            ID3 = 8 

        if id1 == 9:
            self.player.tokensdoubler = self.player.tokensdoubler + multi1
            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
            ID1 = 4
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 9:
            self.player.tokensdoubler = self.player.tokensdoubler + multi2
            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
            ID2 = 4
        if id3 == 9:
            self.player.tokensdoubler = self.player.tokensdoubler + multi3
            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
            ID3 = 4

        if id1 == 8:
            self.player.brawlers_upgradium[str(brawler1)] += multi1
            DataBase.replaceValue(self, 'brawlerUpgradePoints', self.player.brawlers_upgradium)
            ID1 = 5
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 8:
            self.player.brawlers_upgradium[str(brawler2)] += multi2
            DataBase.replaceValue(self, 'brawlerUpgradePoints', self.player.brawlers_upgradium)
            ID2 = 5
        if id3 == 8:
            self.player.brawlers_upgradium[str(brawler3)] += multi3
            DataBase.replaceValue(self, 'brawlerUpgradePoints', self.player.brawlers_upgradium)
            ID3 = 5

        if id1 == 3:
            self.player.BrawlersUnlockedState[str(brawler1)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID1 = 6
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 3:
            self.player.BrawlersUnlockedState[str(brawler2)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID2 = 6
        if id3 == 3:
            self.player.BrawlersUnlockedState[str(brawler3)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID3 = 6

        if id1 == 4:
            self.player.skins[str(skin1)]=1
            DataBase.replaceValue(self, 'skins', self.player.skins)
            ID1 = 7
            Shop.UpdateOfferData(self, self.offer_index)
        if id2 == 4:
            self.player.skins[str(skin2)]=1
            DataBase.replaceValue(self, 'skins', self.player.skins)
            ID2 = 7
        if id3 == 4:
            self.player.skins[str(skin3)]=1
            DataBase.replaceValue(self, 'skins', self.player.skins)
            ID3 = 7

        if id1 == 2:
            brawlers = []
            if skin1 == 0: # Trophy Road
                brawlers = [1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
            if skin1 == 1: # Rare
                brawlers = [6, 10, 13, 24]
            if skin1 == 2: # Super Rare
                brawlers = [4, 18, 19, 25, 34]
            if skin1 == 3: # Epic
                brawlers = [15, 16, 20, 26, 29, 36]
            if skin1 == 4: # Mythic
                brawlers = [11, 17, 21, 31, 32, 37]
            if skin1 == 5: # Legendary
                brawlers = [5, 12, 23, 28, 40]
            if skin1 == 6: # Chromatic
                brawlers = [35, 38, 39, 41]
            brawler1 = brawlers[random.randint(0, len(brawlers) - 1)]
            print('Brawler: ', brawler1)
            while brawler1 not in self.player.brawlers_id or self.player.BrawlersUnlockedState[str(brawler1)] == 1:
                brawler1 = brawlers[random.randint(0, len(brawlers) - 1)]
                print('Brawler: ', brawler1)
            self.player.BrawlersUnlockedState[str(brawler1)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID1 = 6
            Shop.UpdateOfferData(self, self.offer_index)

        if id2 == 2:
            brawlers = []
            if skin2 == 0: # Trophy Road
                brawlers = [1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
            if skin2 == 1: # Rare
                brawlers = [6, 10, 13, 24]
            if skin2 == 2: # Super Rare
                brawlers = [4, 18, 19, 25, 34]
            if skin2 == 3: # Epic
                brawlers = [15, 16, 20, 26, 29, 36]
            if skin2 == 4: # Mythic
                brawlers = [11, 17, 21, 31, 32, 37]
            if skin2 == 5: # Legendary
                brawlers = [5, 12, 23, 28, 40]
            if skin2 == 6: # Chromatic
                brawlers = [35, 38, 39, 41]
            brawler2 = brawlers[random.randint(0, len(brawlers) - 1)]
            print('Brawler: ', brawler2)
            while brawler2 not in self.player.brawlers_id or self.player.BrawlersUnlockedState[str(brawler2)] == 1:
                brawler2 = brawlers[random.randint(0, len(brawlers) - 1)]
                print('Brawler: ', brawler2)
            self.player.BrawlersUnlockedState[str(brawler2)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID2 = 6

        if id3 == 2:
            brawlers = []
            if skin3 == 0: # Trophy Road
                brawlers = [1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
            if skin3 == 1: # Rare
                brawlers = [6, 10, 13, 24]
            if skin3 == 2: # Super Rare
                brawlers = [4, 18, 19, 25, 34]
            if skin3 == 3: # Epic
                brawlers = [15, 16, 20, 26, 29, 36]
            if skin3 == 4: # Mythic
                brawlers = [11, 17, 21, 31, 32, 37]
            if skin3 == 5: # Legendary
                brawlers = [5, 12, 23, 28, 40]
            if skin3 == 6: # Chromatic
                brawlers = [35, 38, 39, 41]
            brawler3 = brawlers[random.randint(0, len(brawlers) - 1)]
            print('Brawler: ', brawler3)
            while brawler3 not in self.player.brawlers_id or self.player.BrawlersUnlockedState[str(brawler3)] == 1:
                brawler3 = brawlers[random.randint(0, len(brawlers) - 1)]
                print('Brawler: ', brawler3)
            self.player.BrawlersUnlockedState[str(brawler3)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID3 = 6





        if id1 in [6, 10, 14]:
            if id1 == 6:
                self.player.box_id = 5
                LogicBoxDataCommand(self.client, self.player).send()
                Shop.UpdateOfferData(self, self.offer_index)
            if id1 == 10:
            	self.player.box_id = 3
            	LogicBoxDataCommand(self.client, self.player).send()
            	Shop.UpdateOfferData(self, self.offer_index)
            if id1 == 14:
                self.player.box_id = 4
                LogicBoxDataCommand(self.client, self.player).send()
                Shop.UpdateOfferData(self, self.offer_index)
        elif id2 in [6, 10, 14]:
            if id2 == 6:
                self.player.box_id = 5
                LogicBoxDataCommand(self.client, self.player).send()
                Shop.UpdateOfferData(self, self.offer_index)
            if id2 == 10:
            	self.player.box_id = 3
            	LogicBoxDataCommand(self.client, self.player).send()
            	Shop.UpdateOfferData(self, self.offer_index)
            if id2 == 14:
                self.player.box_id = 4
                LogicBoxDataCommand(self.client, self.player).send()
                Shop.UpdateOfferData(self, self.offer_index)
        elif id3 in [6, 10, 14]:
            if id3 == 6:
                self.player.box_id = 5
                LogicBoxDataCommand(self.client, self.player).send()
                Shop.UpdateOfferData(self, self.offer_index)
            if id3 == 10:
            	self.player.box_id = 3
            	LogicBoxDataCommand(self.client, self.player).send()
            	Shop.UpdateOfferData(self, self.offer_index)
            if id3 == 14:
                self.player.box_id = 4
                LogicBoxDataCommand(self.client, self.player).send()
                Shop.UpdateOfferData(self, self.offer_index)
        else:
            if id1 != 0 and id2 != 0 and id3 != 0:
                LogicBuyItem(self.client, self.player, ID1, ID2, ID3, multi1, multi2, multi3, brawler1, brawler2, brawler3, skin1, skin2, skin3, pin1, pin2, pin3, accessory1, accessory2, accessory3).send()
            elif id1 != 0 and id2 != 0:
                LogicBuyItem(self.client, self.player, ID1, ID2, 0, multi1, multi2, 0, brawler1, brawler2, 0, skin1, skin2, 0, pin1, pin2, 0, accessory1, accessory2, 0).send()
            else:
                LogicBuyItem(self.client, self.player, ID1, 0, 0, multi1, 0, 0, brawler1, 0, 0, skin1, 0, 0, pin1, 0, 0, accessory1, 0, 0).send()





        #if id == 0:
        #    self.player.box_id = 5
        #    for i in range(multi):
        #        self.player.box_id = 5
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()
        #if id == 6:
        #    self.player.box_id = 5
        #    for i in range(multi):
        #        self.player.box_id = 5
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()
        #if id == 14:
        #    self.player.box_id = 4
        #    for i in range(multi):
        #        self.player.box_id = 4
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()
        #if id == 10:
        #    self.player.box_id = 3
        #    for i in range(multi):
        #        self.player.box_id = 3
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()


