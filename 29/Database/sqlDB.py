import sqlite3 as sql
import hashlib as h
import string as st
import random as r
class VIPDB:
	def __init__(self):
		self.conn = sql.connect("Database/vipkeys.db")
		self.cursor = self.conn.cursor()
	def AddVipKey(self):
		k = "ABCDEFGHIJKLMNOPRSTUWVQXYZqwertyuioplkjhgfdsszxcvbnm1234567890"
		vipkey=""
		for i in range(10):
			vipkey+=r.choice(k)
		self.cursor.execute(f"CREATE TABLE IF NOT EXISTS key (key TEXT)")
		self.conn.commit()
		self.cursor.execute(f"INSERT INTO key VALUES ('{vipkey}')")
		self.conn.commit()
		return vipkey
	def LoadVipKey(self, vipkey):
		self.cursor.execute(f"SELECT key FROM key")
		fetch = self.cursor.fetchone()
		if fetch!=None:
			if fetch[0]==vipkey:
				return vipkey
		else:
			return None
	def GetAllKeys(self):
		self.cursor.execute(f"SELECT key FROM key")
		print(self.cursor.fetchall())
		return self.cursor.fetchall()
	def RemoveVipKey(self, key):
		self.cursor.execute(f"DELETE FROM key WHERE key='{key}'")
		self.conn.commit()
	def AddAdmin(self, token):
		self.cursor.execute(f"CREATE TABLE IF NOT EXISTS admins (token TEXT)")
		self.conn.commit()
		self.cursor.execute(f"INSERT INTO admins VALUES ('{token}')")
		self.conn.commit()
	def LoadAdmin(self, token):
		self.cursor.execute(f"SELECT * FROM admins WHERE token='{token}'")
		return self.cursor.fetchone()
	def LoadFullAdmins(self):
		self.cursor.execute(f"SELECT token FROM admins")
		return self.cursor.fetchall()
class ShopDB:
	def __init__(self):
		self.conn = sql.connect("Database/shop.db")
		self.cursor = self.conn.cursor()
	def LoadOffer(self, token):
		self.cursor.execute(f"SELECT offer FROM shop WHERE token='{token}'")
		return self.cursor.fetchall()
	def AddOffer(self, token, offer):
		self.cursor.execute(f"SELECT offer FROM shop WHERE token='{token}'")
		fetch = self.cursor.fetchall()
		if offer in fetch:
			pass
		else:
				self.cursor.execute(f"INSERT INTO shop VALUES ('{token}', '{offer}')")
				self.conn.commit()
	def Table(self):
		self.cursor.execute(f"CREATE TABLE IF NOT EXISTS shop (token TEXT, offer TEXT)")
		self.conn.commit()
class Leaders:
	def __init__(self):
		pass
	def Table(self):
		self.conn = sql.connect("Database/leaders.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"CREATE TABLE IF NOT EXISTS leaders (token TEXT, lowID INT, name TEXT, trophies INT, club TEXT, clubrole INT, icon INT, color INT)")
		self.conn.commit()
	def AddLeader(self, token, lowID, name, tr, club, r, i, c):
		self.conn = sql.connect("Database/leaders.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"SELECT * FROM leaders WHERE token='{token}'")
		if len(self.cursor.fetchall())==0:
			self.cursor.execute(f"INSERT INTO leaders VALUES ('{token}', {lowID}, '{name}', {tr}, '{club}', {r}, {i}, {c})")
			self.conn.commit()
	def LoadLeader(self, lowID:int=None, token:str=None):
		self.conn = sql.connect("Database/leaders.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"SELECT lowID,name,trophies,icon,color,club FROM leaders ORDER BY trophies DESC")
		return self.cursor.fetchall()
	def UpdateLeader(self, token, trophies):
		self.conn = sql.connect("Database/leaders.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"UPDATE leaders SET trophies=? WHERE token=?", (trophies, token))
		self.conn.commit()
	def UpdateFullLeader(self, token, name, n, i, club, r):
		self.conn = sql.connect("Database/leaders.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"UPDATE leaders SET name='{name}' WHERE token='{token}'")
		self.cursor.execute(f"UPDATE leaders SET color={n} WHERE token='{token}'")
		self.cursor.execute(f"UPDATE leaders SET icon={i} WHERE token='{token}'")
		self.cursor.execute(f"UPDATE leaders SET club='{club}' WHERE token='{token}'")
		self.conn.commit()
		
class ShopOffers:
	def Table(self):
		self.conn = sql.connect("Database/shopoffers.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"CREATE TABLE offers (name TEXT, id INT, cost INT, all INT, brawler INT, skin INT, type INT, disp INT, timer INT)")
		self.conn.commit()
	def LoadAll(self):
		self.conn = sql.connect("Database/shopoffers.db")
		self.cur = self.conn.cursor()
		self.cur.execute("SELECT * FROM offers")
		return  self.cur.fetchall()
	def AddOffer(self, name, ID, cost, amount, brid, skin, type, disp, timer):
		self.conn = sql.connect("Database/shopoffers.db")
		self.cur = self.conn.cursor()
		self.cur.execute("INSERT INTO offers VALUES (?,?,?,?,?,?,?,?,?)", (str(name), ID, cost, amount, brid, skin, type, disp, timer))
		self.conn.commit()
class Link:
	def AddLinkedAccount(self, token, ID):
		self.conn = sql.connect("Database/link.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"CREATE TABLE IF NOT EXISTS link (id INT, token TEXT)")
		self.cur.execute(f"INSERT INTO link VALUES (?,?)", (ID, str(token)))
		self.conn.commit()
		self.conn.close()
	def LoadLink(self, token):
		self.conn = sql.connect("Database/link.db")
		self.cur = self.conn.cursor()
		self.cur.execute(f"SELECT * FROM link WHERE token={token}")
		fetch = self.cur.fetchall()
		if len(fetch)>0:
			return fetch
class ClubLeaders:
	def __init__(self):
		pass
	def Table(self):
		self.conn = sql.connect("Database/clubl.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"CREATE TABLE IF NOT EXISTS leaders (clubID INT, trph INT, name TEXT, members INT, badgeID INT)")
		self.conn.commit()
	def AddLeader(self, ID, tr, name, members, badge):
		self.conn = sql.connect("Database/clubl.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"SELECT * FROM leaders WHERE clubID={ID}")
		if len(self.cursor.fetchall())==0:
			self.cursor.execute(f"INSERT INTO leaders VALUES ({ID}, {tr}, '{name}', {members}, {badge})")
			self.conn.commit()
	def LoadLeader(self, lowID:int=None, token:str=None):
		self.conn = sql.connect("Database/clubl.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"SELECT clubID, trph, name, members, badgeID FROM leaders ORDER BY trph DESC")
		return self.cursor.fetchall()
	def UpdateFullLeader(self, ID, trph, name, members, badgeID):
		self.conn = sql.connect("Database/clubl.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute(f"UPDATE leaders SET name='{name}' WHERE clubID={ID}")
		self.cursor.execute(f"UPDATE leaders SET trph={trph} WHERE clubID={ID}")
		self.cursor.execute(f"UPDATE leaders SET name='{name}' WHERE clubID={ID}")
		self.cursor.execute(f"UPDATE leaders SET members={members} WHERE clubID={ID}")
		self.cursor.execute(f"UPDATE leaders SET badgeID={badgeID} WHERE clubID={ID}")
		self.conn.commit()
class Login:
	def Add(self, ip):
		self.conn = sql.connect("Database/logins.db")
		self.cur=self.conn.cursor()
		self.cur.execute(f"CREATE TABLE IF NOT EXISTS l (ip TEXT)")
		self.cur.execute("INSERT INTO l VALUES (?)", (str(ip)))
		self.conn.commit()
	def Check(self, ip):
		self.conn = sql.connect("Database/logins.db")
		self.cur=self.conn.cursor()
		self.cur.execute("SELECT * FROM l WHERE ip=?", (str(ip)))
		return  self.cur.fetchall()