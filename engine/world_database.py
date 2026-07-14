import json
import os


WORLD_FILE = "world.json"


class WorldDatabase:

    def __init__(self):

        self.data = {
            "rooms": {},
            "npcs": {},
            "quests": {},
            "events": {}
        }

        self.load()


    def load(self):

        if not os.path.exists(WORLD_FILE):
            self.save()
            return

        with open(
            WORLD_FILE,
            "r"
        ) as file:
            self.data = json.load(file)


    def save(self):

        with open(
            WORLD_FILE,
            "w"
        ) as file:
            json.dump(
                self.serialize(self.data),
                file,
                indent=4
            )


    def serialize(self, value):

        if isinstance(value, dict):

            return {
                key: self.serialize(item)
                for key, item in value.items()
            }


        if isinstance(value, list):

            return [
                self.serialize(item)
                for item in value
            ]


        if hasattr(value, "__dict__"):

            return {
                key: self.serialize(item)
                for key, item in value.__dict__.items()
            }


        return value


    def room_exists(
        self,
        room_id
    ):

        return room_id in self.data["rooms"]


    def get_room(
        self,
        room_id
    ):

        return self.data["rooms"].get(
            room_id
        )


    def add_room(
        self,
        room_id,
        room_data
    ):

        self.data["rooms"][room_id] = room_data
        self.save()


    def add_npc(
        self,
        npc_id,
        npc_data
    ):

        self.data["npcs"][npc_id] = npc_data
        self.save()


    def add_quest(
        self,
        quest_id,
        quest_data
    ):

        self.data["quests"][quest_id] = quest_data
        self.save()
