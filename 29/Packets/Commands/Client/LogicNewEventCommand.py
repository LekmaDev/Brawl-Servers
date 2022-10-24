from Utils.Reader import BSMessageReader
from Logic.EventSlots import EventSlots 
from Database.DatabaseManager import DataBase

import json

class LogicNewEventCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.event_index = self.read_Vint()

    def process(self):
        events = EventSlots.loadEvents(self)
        event_index = self.event_index - 1
        if event_index == 0:
            event_slot = events["0"]
        elif event_index == 1:
            event_slot = events["1"]
        elif event_index == 2:
            event_slot = events["2"]
        elif event_index == 3:
            event_slot = events["3"]
        elif event_index == 4:
            event_slot = events["4"]
        elif event_index == 5:
            event_slot = events["5"]
        elif event_index == 6:
            event_slot = events["6"]
        elif event_index == 7:
            event_slot = events["7"]
        elif event_index == 8:
            event_slot = events["8"]
            print(event_slot)
        event_claimed = event_slot['Collected']
        event_tokens = event_slot['Tokens']
        if self.player.token not in event_claimed:
            self.player.brawl_boxes += event_tokens
            DataBase.replaceValue(self, "brawlBoxes", self.player.brawl_boxes)

        #with open("JSON/events.json", "r") as f:
        #    events = json.load(f)
        #if self.player.token not in events['Events'][i]["Collected"]:
        #    events['Events'][i]["Collected"].append(self.player.token)
        #    with open("events.json", "w") as f:
        #        json.dump(events, f, ensure_ascii=False)

        if self.player.low_id not in event_slot["Collected"]:
            event_slot["Collected"].append(self.player.low_id)
            with open("Json/events.json", "w") as f:
                json.dump(events, f, ensure_ascii=False)








