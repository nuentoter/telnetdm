from engine.objects.item import Item
from engine.loot import LootDrop, generate_loot



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



    def generate_loot(self):

        return generate_loot(

            self.loot

        )





def create_creature(creature_id):


    if creature_id == "forest_wolf":


        wolf_fang = Item(

            item_id="wolf_fang",

            name="wolf fang",

            aliases=[

                "fang",

                "tooth"

            ],

            description=(

                "A sharp fang taken from a forest wolf."

            ),

            weight=0.1,

            value=5

        )


        return Creature(

            creature_id="forest_wolf",

            name="Forest Wolf",

            description=(

                "A large gray predator watching "

                "with hungry eyes."

            ),

            hp=12,

            xp_reward=50,

            loot=[

                LootDrop(

                    item=wolf_fang,

                    chance=1.0

                ),

                LootDrop(

                    gold_min=3,

                    gold_max=10,

                    chance=0.75

                )

            ]

        )


    return None
