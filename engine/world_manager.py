from engine.world import WORLD



class WorldManager:

    def __init__(self):

        self.rooms = WORLD



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


        player.room = room.exits[direction]

        return True



    def remove_item(
        self,
        room_id,
        item
    ):

        room = self.get_room(
            room_id
        )


        if not room:

            return False


        return room.remove_item(
            item
        )



    def add_item(
        self,
        room_id,
        item
    ):

        room = self.get_room(
            room_id
        )


        if not room:

            return False


        room.add_item(
            item
        )


        return True
