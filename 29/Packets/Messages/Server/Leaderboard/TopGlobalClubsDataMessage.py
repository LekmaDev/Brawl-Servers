from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class  GetLeaderboardClubGlobalOkMessage(Writer):

    def __init__(self, client, player, type):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.type = type

    def encode(self):
        self.indexOfClub = 0
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()
        self.writeVint(0)
        for club in range(0):
            if club[0] == self.player.club_low_id:
                self.indexOfClub += 1
            self.writeVint(0) # Club High ID
            self.writeVint(club[0]) # Club Low ID

            self.writeVint(1)
            self.writeVint(club[1]) # Club Trophies
            self.writeVint(2)

            self.writeString(club[2]) # Club Name
            self.writeVint(club[3]) # Club Members Count

            self.writeVint(8) # Club Badge
            self.writeVint(club[4]) # Club Name Color

        self.writeVint(0)
        self.writeVint(self.indexOfClub) # Index of the club
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.player.region)