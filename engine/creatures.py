from objects.monster import Monster



CREATURES = {


    "forest_wolf":

        lambda:

        Monster(

            "forest_wolf",

            "Forest Wolf",

            hp=12,

            damage=3,

            xp=50

        ),



    "goblin":

        lambda:

        Monster(

            "goblin",

            "Goblin",

            hp=8,

            damage=2,

            xp=35

        )

}



def create_creature(
    creature_id
):

    creature = CREATURES.get(
        creature_id
    )


    if creature:

        return creature()


    return None
