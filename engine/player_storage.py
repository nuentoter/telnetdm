import json
import os


PLAYER_FILE = "players.json"



def save_player(player):

    data = player.describe()


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

        return json.load(file)



def apply_saved_player(
    player,
    data
):

    player.name = data.get(
        "name",
        "Adventurer"
    )


    player.class_name = data.get(
        "class",
        "fighter"
    )


    player.room = data.get(
        "room",
        "start_room"
    )


    player.level = data.get(
        "level",
        1
    )


    player.experience = data.get(
        "experience",
        0
    )


    player.hp = data.get(
        "hp",
        10
    )


    player.max_hp = data.get(
        "max_hp",
        10
    )


    return player
