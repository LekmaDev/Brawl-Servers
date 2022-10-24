from Utils.Reader import BSMessageReader
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters

class LogicClearShopTickersCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()      


    def process(self):
        pass