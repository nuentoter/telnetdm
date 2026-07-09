from engine.entity import Entity



class Monster(Entity):


    def __init__(

        self,

        entity_id,

        name,

        hp=10,

        damage=2,

        xp=25

    ):

        super().__init__(

            entity_id,

            name

        )


        self.hp = hp

        self.max_hp = hp

        self.damage = damage

        self.xp_reward = xp



    def describe(self):

        return (

            f"{self.name}\r\n"

            f"HP: {self.hp}/{self.max_hp}"

        )
