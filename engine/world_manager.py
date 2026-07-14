import random
import uuid

from engine.world_database import WorldDatabase
from engine.world_seed import seed_world
from engine.npc_factory import create_npcs


class WorldManager:

    def __init__(self, registry):

        self.registry = registry
        self.database = WorldDatabase()

        seed_world(self.database)

        self.current_world = self.database.data


    def get_room(self, room_id):

        room = self.database.get_room(room_id)

        if room is None:
            return self.create_unknown_room(room_id)

        if isinstance(room.get("npcs"), list):
            room["npcs"] = create_npcs(room["npcs"])

        return room


    def create_unknown_room(self, room_id):

        room = {
            "id": room_id,
            "name": "Unexplored Territory",
            "description": "A place no map has recorded yet.",
            "exits": {},
            "items": [],
            "npcs": []
        }

        self.database.add_room(
            room_id,
            room
        )

        return room


    def generate_room(self, from_room, direction):

        room_id = "room_" + str(uuid.uuid4())[:8]

        names = [
            "Forgotten Grove",
            "Ancient Crossing",
            "Misty Hollow",
            "Silent Ruins",
            "Hidden Valley"
        ]

        descriptions = [
            "The land beyond is untouched by civilization.",
            "Old stones and strange markings cover the ground.",
            "The wilderness stretches farther than expected."
        ]

        reverse = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east"
        }

        room = {
            "id": room_id,
            "name": random.choice(names),
            "description": random.choice(descriptions),
            "exits": {
                reverse[direction]: from_room
            },
            "items": [],
            "npcs": []
        }

        self.database.add_room(
            room_id,
            room
        )

        origin = self.get_room(from_room)
        origin["exits"][direction] = room_id

        self.database.save()

        return room_id


    def room_exists(self, room_id):

        return self.database.room_exists(room_id)


    def move_player(self, player, direction):

        room = self.get_room(player.room)

        if direction not in room["exits"]:
            self.generate_room(
                player.room,
                direction
            )

        player.room = room["exits"][direction]

        return True


    def add_item(self, room_id, item):

        room = self.get_room(room_id)
        room["items"].append(item)
        self.database.save()


    def remove_item(self, room_id, item):

        room = self.get_room(room_id)

        if item in room["items"]:
            room["items"].remove(item)

        self.database.save()
