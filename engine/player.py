class Player:

    def __init__(self, name="Adventurer"):

        self.id = None

        self.name = name

        self.room = "ruined_outpost"

        self.inventory = []


        # Future D&D style data

        self.level = 1

        self.experience = 0


        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }


        self.class_name = None



    def add_item(self, item):

        self.inventory.append(item)



    def remove_item(self, item):

        if item in self.inventory:

            self.inventory.remove(item)



    def has_item(self, item):

        return item in self.inventory



    def describe(self):

        return {

            "id": self.id,

            "name": self.name,

            "room": self.room,

            "inventory": self.inventory,

            "level": self.level,

            "experience": self.experience,

            "stats": self.stats,

            "class": self.class_name

        }
