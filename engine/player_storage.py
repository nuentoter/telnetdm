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
