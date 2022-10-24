from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage

class BattleLogMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeBoolean(False)
        self.writeVInt(0)

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(23458, fields, calling_instance.player)

    def getMessageType(self):
        return 23458

    def getMessageVersion(self):
        return self.messageVersion