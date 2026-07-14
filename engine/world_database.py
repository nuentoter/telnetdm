import json
import os
import shutil


WORLD_FILE = "world.json"
BACKUP_FILE = "world.json.backup"
WORLD_VERSION = 1


class WorldDatabase:

    def __init__(self):

        self.data = {
            "version": WORLD_VERSION,
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

        try:
            with open(
                WORLD_FILE,
                "r"
            ) as file:
                self.data = json.load(file)

        except json.JSONDecodeError:

            if os.path.exists(BACKUP_FILE):

                shutil.copy(
                    BACKUP_FILE,
                    WORLD_FILE
                )

                with open(
                    WORLD_FILE,
                    "r"
                ) as file:
                    self.data = json.load(file)

            else:
                self.save()


        if "version" not in self.data:
            self.data["version"] = WORLD_VERSION


    def save(self):

        serialized = self.serialize(
            self.data
        )

        if os.path.exists(WORLD_FILE):
            shutil.copy(
                WORLD_FILE,
                BACKUP_FILE
            )

        with open(
            WORLD_FILE,
            "w"
        ) as file:
            json.dump(
                serialized,
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
