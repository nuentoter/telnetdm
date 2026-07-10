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

        attack_total = (
            attack_roll
            + self.player.stats.modifier(
                "strength"
            )
        )

        critical = (
            attack_roll == 20
        )
weapon = player.equipment["weapon"]

if weapon:

    damage = roll(
        weapon.damage
    )[0]

else:

    damage = roll(4)[0]

        if critical:
            damage *= 2

        self.enemy.hp -= damage

        return {
            "hit": attack_total >= 10,
            "critical": critical,
            "attack_roll": attack_roll,
            "damage": damage,
            "enemy_hp": max(
                self.enemy.hp,
                0
            )
        }


    def enemy_attack(self):

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
