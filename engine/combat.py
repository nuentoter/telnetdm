from engine.dice import roll



class Combat:


    def __init__(
        self,
        player,
        enemy
    ):

        self.player = player

        self.enemy = enemy



    def player_attack(self):

        attack = roll(
            20
        )[0]


        damage = roll(
            6
        )[0]


        self.enemy.hp -= damage


        return {

            "attack": attack,

            "damage": damage,

            "enemy_hp": self.enemy.hp

        }



    def enemy_attack(self):

        damage = roll(
            4
        )[0]


        self.player.hp -= damage


        return {

            "damage": damage,

            "player_hp": self.player.hp

        }



    def finished(self):

        return (

            self.player.hp <= 0

            or

            self.enemy.hp <= 0

        )
