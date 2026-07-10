from engine.resolver import resolve_item
from engine.npc_resolver import resolve_npc
from engine.encounter import check_encounter
from engine.combat import Combat



ACTION_TABLE = {}



def action(name):

    def decorator(func):

        ACTION_TABLE[name] = func

        return func

    return decorator





def execute_action(

    session,

    action,

    world

):

    func = ACTION_TABLE.get(

        action.type

    )


    if func:

        return func(

            session,

            action,

            world

        )


    return "Nothing happens."





@action("look")
def do_look(

    session,

    action,

    world

):

    room = world.get_room(

        session.player.room

    )


    return room.describe()





@action("move")
def do_move(

    session,

    action,

    world

):

    if not world.move_player(

        session.player,

        action.target

    ):

        return "You cannot go that way."


    room = world.get_room(

        session.player.room

    )


    result = room.describe()


    encounter = check_encounter(

        room.id

    )


    if encounter:

        session.combat = Combat(

            session.player,

            encounter

        )


        result += (

            "\r\n\r\n"

            f"A {encounter.name} appears!"

            "\r\n"

            "Type: attack"

        )


    return result





@action("attack")
def do_attack(

    session,

    action,

    world

):

    if session.combat is None:

        return "There is nothing to attack."



    result = session.combat.player_attack()


    output = []



    if result["hit"]:

        if result["critical"]:

            output.append(

                "Critical hit!"

            )


        output.append(

            f"You hit the "

            f"{session.combat.enemy.name} "

            f"for {result['damage']} damage."

        )


    else:

        output.append(

            "You miss."

        )



    if session.combat.enemy.hp <= 0:


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


        loot = enemy.generate_loot()


        for item in loot["items"]:

            session.player.add_item(

                item

            )


            output.append(

                f"You found: {item.name}"

            )


        if loot["gold"] > 0:

            session.player.gold += loot["gold"]


            output.append(

                f"You found {loot['gold']} gold."

            )


        session.combat = None


        return "\r\n".join(

            output

        )



    enemy_result = session.combat.enemy_attack()



    if enemy_result["hit"]:

        output.append(

            f"The "

            f"{session.combat.enemy.name} "

            f"hits you for "

            f"{enemy_result['damage']} damage."

        )

    else:

        output.append(

            f"The "

            f"{session.combat.enemy.name} "

            f"misses."

        )



    if session.player.hp <= 0:

        session.player.hp = 1

        session.combat = None


        output.append(

            "You collapse from your wounds."

        )


        return "\r\n".join(

            output

        )



    output.append(

        f"HP: "

        f"{session.player.hp}/"

        f"{session.player.max_hp}"

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





@action("take")
def do_take(

    session,

    action,

    world

):

    room = world.get_room(

        session.player.room

    )


    item = resolve_item(

        action.target,

        room.items

    )


    if not item:

        return "You don't see that here."



    world.remove_item(

        room.id,

        item

    )


    session.player.add_item(

        item

    )


    return f"You take the {item.name}."





@action("drop")
def do_drop(

    session,

    action,

    world

):

    item = resolve_item(

        action.target,

        session.player.inventory

    )


    if not item:

        return "You aren't carrying that."



    session.player.inventory.remove(

        item

    )


    world.add_item(

        session.player.room,

        item

    )


    return f"You drop the {item.name}."





@action("inventory")
def do_inventory(

    session,

    action,

    world

):

    lines = []


    lines.append(

        f"Gold: {session.player.gold}"

    )


    if not session.player.inventory:

        lines.append(

            "You are carrying nothing."

        )


        return "\r\n".join(

            lines

        )



    lines.append(

        "You are carrying:"

    )


    for item in session.player.inventory:

        lines.append(

            f" - {item.name}"

        )


    return "\r\n".join(

        lines

    )





@action("talk")
def do_talk(

    session,

    action,

    world

):

    room = world.get_room(

        session.player.room

    )


    npc = resolve_npc(

        action.target,

        room.npcs

    )


    if not npc:

        return "Nobody by that name is here."


    return npc.speak()
