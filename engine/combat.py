from engine.dice import roll



class Combat:

    def __init__(

        self,

        player,

        enemy

    ):

        self.player = player
        self.enemy = enemy
        self.round = 1



    def player_attack(self):

        attack_roll = roll(20)[0]


        strength_bonus = (

            self.player.stats.modifier(
                "strength"
            )

        )


        attack_total = (

            attack_roll

            +

            strength_bonus

        )


        critical = (

            attack_roll == 20

        )


        weapon = self.player.equipment.get(
            "weapon"
        )


        if weapon:

            damage = roll(
                weapon.damage
            )[0]

        else:

            damage = roll(4)[0]



        if critical:

            damage *= 2



        hit = attack_total >= 10



        if hit:

            self.enemy.hp -= damage


        return {

            "hit": hit,

            "critical": critical,

            "attack_roll": attack_roll,

            "damage": damage if hit else 0,

            "enemy_hp": max(
                self.enemy.hp,
                0
            )

        }



    def enemy_attack(self):

        if self.enemy.hp <= 0:

            return {

                "hit": False,

                "damage": 0,

                "player_hp": self.player.hp

            }



        attack_roll = roll(20)[0]


        hit = attack_roll >= 8


        damage = 0


        if hit:

            damage = roll(4)[0]

            self.player.hp -= damage



        return {

            "hit": hit,

            "attack_roll": attack_roll,

            "damage": damage,

            "player_hp": max(

                self.player.hp,

                0

            )

        }



    def finished(self):

        return (

            self.player.hp <= 0

            or

            self.enemy.hp <= 0

        )
