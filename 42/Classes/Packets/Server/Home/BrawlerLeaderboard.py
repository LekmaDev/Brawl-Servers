from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler

class BrawlerLeaderboard(PiranhaMessage):

    def __init__(self, messageData, brawler=0):
        super().__init__(messageData)
        self.messageVersion = 0
        self.brawler = brawler

    def encode(self):
        db = DatabaseHandler()
        #data = db.sortPlayers('trophies')
        data = db.getSorted('Trophies')
        self.writeVInt(0)
        self.writeVInt(16)
        self.writeVInt(self.brawler)
        self.writeString()

        self.writeVInt(1) # Players Count

        for i in range(1):
            self.writeVInt(0) # High ID
            self.writeVInt(data[i]["ID"]) # Low ID

            self.writeVInt(1)
            self.writeVInt(6974) # Player Trophies

            self.writeVInt(1)

            self.writeString()
                
            self.writeString(data[i]["name"]) # Player Name
            self.writeVInt(0) # Player Level
            self.writeVInt(28000000 + self.brawler)
            self.writeVInt(43000000 + data[i]["cname"])
            self.writeVInt(0)
            self.writeVInt(0) # Unknown


        self.writeVInt(0)
        for i in data:
        	if i["ID"] == self.player.ID:
        		self.writeVInt(data.index(i) + 1)
        self.writeVInt(1)
        self.writeVInt(0) # Leaderboard global TID
        self.writeString("RU")

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24403

    def getMessageVersion(self):
        return self.messageVersion