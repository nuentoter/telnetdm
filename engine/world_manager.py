from engine.world_database import WorldDatabase
from engine.world_seed import seed_world


class WorldManager:

    def __init__(self, registry):

        self.registry = registry

        self.database = WorldDatabase()

        seed_world()

        self.current_world = self.database.data


        # force first room
        if not self.database.room_exists("forest_edge"):

            seed_world()



    def get_room(self, room_id):

        room = self.database.get_room(room_id)


        if room is None:

            return self.create_unknown_room(room_id)


        return room



    def create_unknown_room(self, room_id):

        room = {

            "id": room_id,

            "name": "Unknown Place",

            "description":
                "An unexplored place waits beyond.",

            "exits": {},

            "items": [],

            "npcs": []

        }


        self.database.add_room(

            room_id,

            room

        )


        return room



    def room_exists(self, room_id):

        return self.database.room_exists(room_id)



    def move_player(self, player, direction):

        room = self.get_room(

            player.room

        )


        if direction not in room["exits"]:

            return False


        player.room = room["exits"][direction]


        if not self.room_exists(player.room):

            self.create_unknown_room(

                player.room

            )


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
