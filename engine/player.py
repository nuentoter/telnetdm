class Player:

    def __init__(self, name="Adventurer"):

        self.name = name

        self.room = "ruined_outpost"

        self.inventory = []


    def describe(self):

        return {
            "name": self.name,
            "room": self.room,
            "inventory": self.inventory
        }
