import random

from engine.creatures import create_creature


ENCOUNTERS = {

    "forest_edge": [

        "forest_wolf"

    ]

}



def check_encounter(
    room_id
):

    creatures = ENCOUNTERS.get(
        room_id
    )


    if not creatures:

        return None


    if random.random() > 0.9:

        return None


    creature_id = random.choice(
        creatures
    )


    return create_creature(
        creature_id
    )
