from engine.objects.item import Item



class Creature:

    def __init__(

        self,

        creature_id,

        name,

        description,

        hp,

        xp_reward,

        loot=None

    ):

        self.id = creature_id

        self.name = name

        self.description = description

        self.max_hp = hp

        self.hp = hp

        self.xp_reward = xp_reward

        self.loot = loot or []



    def describe(self):

        return (

            f"{self.name}\r\n"

            f"HP: {self.hp}/{self.max_hp}\r\n"

            f"{self.description}"

        )



def create_creature(creature_id):


    if creature_id == "forest_wolf":


        return Creature(

            creature_id="forest_wolf",

            name="Forest Wolf",

            description=(

                "A large gray predator "

                "watching with hungry eyes."

            ),

            hp=12,

            xp_reward=50,

            loot=[

                Item(

                    "wolf_fang",

                    "wolf fang",

                    [

                        "fang",

                        "tooth"

                    ],

                    "A sharp fang taken from a forest wolf.",

                    value=5

                )

            ]

        )


    return None
