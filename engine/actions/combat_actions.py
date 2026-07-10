from engine.action_handler import action
from engine.resolver import resolve_item



@action("attack")
def do_attack(

    session,

    action,

    world

):

    if session.combat is None:

        return "There is nothing to attack."


    output = []


    result = session.combat.player_attack()


    if result["hit"]:

        if result["critical"]:

            output.append(

                "Critical hit!"

            )


        output.append(

            f"You hit the {session.combat.enemy.name} "
            f"for {result['damage']} damage."

        )


    else:

        output.append(

            "You miss."

        )


    if session.combat.finished():

        enemy = session.combat.enemy

        xp = enemy.xp_reward

        enemy_name = enemy.name


        session.player.gain_xp(

            xp

        )


        output.append(

            f"You defeated the {enemy_name}!"

        )


        output.append(

            f"You gain {xp} XP."

        )


        if getattr(enemy, "loot", None):

            for loot in enemy.loot:

                item = loot.item


                session.player.add_item(

                    item

                )


                output.append(

                    f"You found: {item.name}"

                )


        session.combat = None


        return "\r\n".join(

            output

        )


    enemy_result = session.combat.enemy_attack()


    if enemy_result["hit"]:

        output.append(

            f"The {session.combat.enemy.name} "
            f"hits you for {enemy_result['damage']} damage."

        )

    else:

        output.append(

            f"The {session.combat.enemy.name} misses."

        )


    output.append(

        f"HP: {session.player.hp}/{session.player.max_hp}"

    )


    return "\r\n".join(

        output

    )



@action("enemy")
def do_enemy(

    session,

    action,

    world

):

    if session.combat is None:

        return "There is no enemy."


    return session.combat.enemy.describe()



@action("flee")
def do_flee(

    session,

    action,

    world

):

    if session.combat is None:

        return "You are not fighting."


    session.combat = None


    return "You flee from combat."
