from engine.world import WORLD


class WorldManager:

    def __init__(
        self,
        registry
    ):

        self.registry = registry

        self.rooms = WORLD


        self._register_world()



    def _register_world(self):

        for room in self.rooms.values():

            self.registry.register(
                room
            )


            for item in room.items:

                self.registry.register(
                    item
                )


            for npc in room.npcs:

                self.registry.register(
                    npc
                )



    def get_room(
        self,
        room_id
    ):

        return self.rooms.get(
            room_id
        )



    def move_player(
        self,
        player,
        direction
    ):

        room = self.get_room(
            player.room
        )


        if not room:

            return False


        if direction not in room.exits:

            return False


        player.room = room.exits[
            direction
        ]

        return True



    def add_item(
        self,
        room_id,
        item
    ):

        room = self.get_room(
            room_id
        )


        if room:

            room.add_item(
                item
            )

            return True


        return False



    def remove_item(
        self,
        room_id,
        item
    ):

        room = self.get_room(
            room_id
        )


        if room:

            return room.remove_item(
                item
            )


        return False
