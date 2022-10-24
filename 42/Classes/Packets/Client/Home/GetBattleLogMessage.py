from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class GetBattleLogMessage(PiranhaMessage):
    def init(self, messageData):
        super().init(messageData)
        self.messageVersion = 0

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(23458, fields, calling_instance.player)

    def getMessageType(self):
        return 14114

    def getMessageVersion(self):
        return self.messageVersion