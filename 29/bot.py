import logging
import socket
import time
import os
from threading import *
import colorama
import requests
from html import escape
import os
from Logic.Device import Device
from Logic.Player import Players
from Packets.LogicMessageFactory import packets
from Utils.Config import Config

#logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")
print(f'speedinstall.sh installed Version 1.0') 
red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.CYAN
purple = colorama.Fore.MAGENTA
sam = {}
def _(*args):
	
	print(f'{purple}[{red}CLIENT{purple}]{blue}', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()

class Server:
	Clients = {"ClientCounts": 0, "Clients": {}}
	ThreadCount = 0


	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		if not os.path.exists('./config.json'):
			print("Creating config.json...")
			Config.create_config(self)
			



		self.server.bind((self.ip, self.port))
		
		print(f'{purple}[{red}INFO{purple}]{blue}{blue} Server Started! IP: {green}{self.ip}{blue}, PORT: {green}{self.port}')
		print(f'{purple}[{red}INFO{purple}]{blue} {blue}Players Online: {green}{Server.ThreadCount}')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			_(f'New Connect! IP: {green}{address[0]}')
			ClientThread(client, address).start()
			Server.ThreadCount += 1
			_(f'{blue}Players Online! {green}{Server.ThreadCount}')

class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)
		self.dudu = []
	def ban_ip(self, ip: str, dudu: list):
		if ip not in dudu:
			dudu.append(ip)
			with open('banned_ips.txt', 'a') as f:
				f.write(ip + '\n')
				print('дудник забанен')
			return True
		else:
			print('ты чё долбоёб')
			return False
	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		if self.address[0] in sam:
			if (time.time() - sam[self.address[0]]) < 5:
				if self.address[0] in self.dudu:
					self.client.close()
					Server.ThreadCount -= 1
					_(f'{blue}Players Online: {green}{Server.ThreadCount}')
					return
				else:
					self.dudu.append(self.address[0])
					print(f'{red}[ANTIDDOS] Эта Шлюха тя ддосит ---> {self.address[0]}{green}')
					ban_ip(self.address[0], self.dudu)
					self.client.close()
					Server.ThreadCount -= 1
					_(f'{blue}Players Online: {green}{Server.ThreadCount}')
					return
		sam[self.address[0]] = time.time()
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)
					if packet_id in packets:
						_(f'Used Packet! ID: {green}{packet_id}')
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()

						if packet_id == 10101:
							Server.Clients["Clients"][str(self.player.low_id)] = {"SocketInfo": self.client}
							Server.Clients["ClientCounts"] = Server.ThreadCount
							self.player.ClientDict = Server.Clients
					else:
						_(f'404 packet error! ID: {green}{packet_id}')

				if time.time() - last_packet > 10:
					_(f"IP: {green}{self.address[0]}{blue} disconnected!")
					Server.ThreadCount -= 1
					_(f'{blue}Players Online: {green}{Server.ThreadCount}')
					self.client.close()
					break
		except ConnectionAbortedError:
			_(f"IP: {green}{self.address[0]}{blue} disconnected! {red}ConnectionAbortedError")
			Server.ThreadCount -= 1
			_(f'{blue}Players Online: {green}{Server.ThreadCount}')
			self.client.close()
		except ConnectionResetError:
			_(f"IP: {green}{self.address[0]}{blue} disconnectrd! {red}ConnectionResetError")
			Server.ThreadCount -= 1
			_(f'{blue}Players Online: {green}{Server.ThreadCount}')
			self.client.close()
		except TimeoutError:
			_(f"IP: {green}{self.address[0]}{blue} disconnectd! {red}TimeoutError")
			Server.ThreadCount -= 1
			_(f'{blue}Players Online: {green}{Server.ThreadCount}')
			self.client.close()
			




if __name__ == '__main__':
	try:
		server = Server('0.0.0.0', 5128)
		server.start()
	except Exception as e:
		_(f'{blue}Port {red}"{green}9333{red}"{blue} enisss{red}\n\n{green}WHAT??? GENE???:\n{purple}{e}{red}')
        
