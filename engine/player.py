from engine.stats import Stats



class Player:


    def __init__(

        self,

        name="Adventurer",

        class_name="fighter"

    ):

        self.name = name

        self.class_name = class_name

        self.room = "start_room"


        self.level = 1

        self.experience = 0


        self.stats = Stats()


        self.max_hp = 10

        self.hp = self.max_hp


        self.inventory = []


        self.equipment = {

            "head": None,

            "chest": None,

            "legs": None,

            "feet": None,

            "hands": None,

            "weapon": None,

            "offhand": None,

            "ring_left": None,

            "ring_right": None,

            "neck": None

        }



    def add_item(

        self,

        item

    ):

        self.inventory.append(
            item
        )



    def remove_item(

        self,

        item

    ):

        if item in self.inventory:

            self.inventory.remove(
                item
            )



    def equip(

        self,

        item

    ):

        if not item.slot:

            return False


        self.equipment[item.slot] = item

        return True



    def unequip(

        self,

        slot

    ):

        item = self.equipment.get(
            slot
        )

        self.equipment[slot] = None

        return item



    def gain_xp(

        self,

        amount

    ):

        self.experience += amount


        if self.experience >= self.level * 100:

            self.level_up()



    def level_up(self):

        self.level += 1

        self.max_hp += 5

        self.hp = self.max_hp



    def describe(self):

        return {

            "name": self.name,

            "class": self.class_name,

            "room": self.room,

            "level": self.level,

            "experience": self.experience,

            "hp": self.hp,

            "max_hp": self.max_hp,

            "stats": self.stats.describe(),

            "inventory": [

                item.id

                for item in self.inventory

            ],

            "equipment": {

                slot:

                item.id if item else None

                for slot, item

                in self.equipment.items()

            }

        }
