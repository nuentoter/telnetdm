import json
import os

from engine.world import WORLD


PLAYER_FILE = "players.json"



def find_item(item_id):

    for room in WORLD.values():

        for item in room.items:

            if item.id == item_id:

                return item

    return None



def save_player(player):

    data = {

        "room": player.room,

        "inventory": [

            item.id

            for item in player.inventory

        ]

    }


    with open(
        PLAYER_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



def load_player():

    if not os.path.exists(
        PLAYER_FILE
    ):

        return None


    with open(
        PLAYER_FILE,
        "r"
    ) as file:

        data = json.load(file)


    restored_inventory = []


    for item_id in data.get(
        "inventory",
        []
    ):

        item = find_item(
            item_id
        )


        if item:

            restored_inventory.append(
                item
            )


    data["inventory"] = restored_inventory


    return data
