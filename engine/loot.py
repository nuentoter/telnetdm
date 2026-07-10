import random



class LootDrop:

    def __init__(

        self,

        item=None,

        gold_min=0,

        gold_max=0,

        chance=1.0

    ):

        self.item = item

        self.gold_min = gold_min

        self.gold_max = gold_max

        self.chance = chance



    def roll(self):

        if random.random() > self.chance:

            return None


        gold = 0


        if self.gold_max > 0:

            gold = random.randint(

                self.gold_min,

                self.gold_max

            )


        return {

            "item": self.item,

            "gold": gold

        }



def generate_loot(table):

    results = []


    total_gold = 0


    for drop in table:

        result = drop.roll()


        if not result:

            continue


        if result["item"]:

            results.append(

                result["item"]

            )


        total_gold += result["gold"]



    return {

        "items": results,

        "gold": total_gold

    }
