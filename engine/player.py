class Player:

    def __init__(
        self,
        name="Adventurer"
    ):

        self.name = name

        self.room = "start_room"

        self.level = 1

        self.experience = 0

        self.gold = 0


        self.max_hp = 15

        self.hp = self.max_hp


        self.stats = Stats()


        self.inventory = []


        self.equipment = {

            "weapon": None,

            "armor": None

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


        old_item = self.equipment.get(
            item.slot
        )


        if old_item:

            self.inventory.append(
                old_item
            )


        self.inventory.remove(
            item
        )


        self.equipment[item.slot] = item


        return True



    def unequip(
        self,
        slot
    ):

        item = self.equipment.get(
            slot
        )


        if item:

            self.inventory.append(
                item
            )

            self.equipment[slot] = None


            return item


        return None



    def gain_xp(
        self,
        amount
    ):

        self.experience += amount


        while self.experience >= self.level * 100:

            self.experience -= self.level * 100

            self.level += 1

            self.max_hp += 5

            self.hp = self.max_hp



    def heal(
        self,
        amount
    ):

        self.hp = min(

            self.hp + amount,

            self.max_hp

        )



    def describe(self):

        return {

            "name": self.name,

            "room": self.room,

            "level": self.level,

            "experience": self.experience,

            "gold": self.gold,

            "hp": self.hp,

            "max_hp": self.max_hp,

            "inventory": [

                item.name

                for item in self.inventory

            ],

            "equipment": {

                slot:

                item.name if item else None

                for slot, item in self.equipment.items()

            }

        }



class Stats:

    def __init__(self):

        self.values = {

            "strength": 10,

            "dexterity": 10,

            "constitution": 10,

            "intelligence": 10,

            "wisdom": 10,

            "charisma": 10

        }



    def modifier(
        self,
        stat
    ):

        value = self.values.get(

            stat,

            10

        )


        return (

            value - 10

        ) // 2



    def describe(self):

        return self.values
