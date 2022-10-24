import json
import random

class OfferGenerator:
	def generateDailyGift(brawlersUnlocked = []):
		result = []
		free = random.choice(["powerpoints", "gem", "box"])
		result.append({})
		brawler = 0
		if free == "gem":
			type = 16
			count = random.randint(1, 3)
		elif free == "powerpoints":
			type = 8
			count = random.randint(4, 8)
			brawler = random.choice(brawlersUnlocked)
		elif free == "tokendoubler":
			type = 9
			count = random.choice([16, 24])
		elif free == "coins":
			type = 1
			count = random.choice([12, 16, 20, 24])
		elif free == "box":
			type = 0
			count = 1
		result[0] = {"OfferTitle": "БЕСПЛАТНЫЙ ПОДАРОК", "Cost": 0, "OldCost": 0, "ID": type, "Multiplier": count, "csvID": 16, "BrawlerID": brawler, "SkinID": 0, "ShopType": 1, "ShopDisplay": 1, "Timer": 86400, "DBID": "Free-%s-%i" % (free, random.randint(1, 999999999))} # free
		return result[0] #json.dumps(result)
	
	def generateOffersList(brawlersUnlocked = [], max = 5):
		result = []
		ind = 0
		random.shuffle(brawlersUnlocked)
		for brawler in brawlersUnlocked:
			if ind < max:
				powerpoints = random.randint(3, 25)
				gene = {"OfferTitle": "ОЧКИ СИЛЫ", "Cost": powerpoints * 2, "OldCost": 0, "ID": 8, "Multiplier": powerpoints, "csvID": 16, "BrawlerID": brawler, "SkinID": 0, "ShopType": 1, "ShopDisplay": 1, "Timer": 86400, "DBID": "PowerPoints-%i" % random.randint(1, 999999999)}
				result.append(gene)
				ind += 1
			else:
				break
		return result