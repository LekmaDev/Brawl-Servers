    def sendByID(self, ID):
        try:
            self.encode()
            packet = self.buffer
            self.buffer = self.id.to_bytes(2, 'big', signed=True)
            self.writeInt(len(packet), 3)
            if hasattr(self, 'version'):
                self.writeInt16(self.version)
            else:
                self.writeInt16(0)
            self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
            Helpers.connected_clients["Clients"][str(ID)]["SocketInfo"].send(self.buffer)
        except Exception as e:
            print(e)