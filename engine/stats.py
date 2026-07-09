class Stats:

    def __init__(
        self,
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10
    ):

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma



    def modifier(self, stat):

        value = getattr(
            self,
            stat,
            10
        )

        return (value - 10) // 2



    def describe(self):

        return {

            "strength": self.strength,

            "dexterity": self.dexterity,

            "constitution": self.constitution,

            "intelligence": self.intelligence,

            "wisdom": self.wisdom,

            "charisma": self.charisma

        }
