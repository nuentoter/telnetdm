class Player:
    def __init__(self):
        self.name = "Wanderer"

        self.level = 1

        self.max_hp = 10
        self.current_hp = 10

        self.room = "start_room"

        self.inventory = []

        # Basic ability scores (very simplified D&D-style)
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
