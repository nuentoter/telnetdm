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


@action("equip")

@action("unequip")



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


@action("attack")
def do_attack(
    session,
    action,
    world
):

    if session.combat is None:

        return (
            "There is nothing to attack."
        )


    result = session.combat.player_attack()


    output = []


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

        xp = session.combat.enemy.xp_reward

        session.player.gain_xp(
            xp
        )

        enemy_name = (
            session.combat.enemy.name
        )

        session.combat = None

        output.append(
            f"You defeated the {enemy_name}!"
        )

        output.append(
            f"You gain {xp} XP."
        )

        output.append(
            f"Level: {session.player.level}"
        )

        return "\r\n".join(
            output
        )


    enemy = session.combat.enemy_attack()


    if enemy["hit"]:

        output.append(

            f"The {session.combat.enemy.name} "

            f"hits you for {enemy['damage']} damage."

        )

    else:

        output.append(

            f"The {session.combat.enemy.name} misses."

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

        return (
            "There is no enemy."
        )

    return session.combat.enemy.describe()


@action("flee")
def do_flee(
    session,
    action,
    world
):

    if session.combat is None:

        return (
            "You are not fighting."
        )

    session.combat = None

    return (
        "You flee from combat."
    )


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

    if not world.move_player(

        session.player,

        action.target

    ):

        return "You cannot go that way."

    return world.get_room(

        session.player.room

    ).describe()


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

    if not session.player.inventory:

        return "You are carrying nothing."

    lines = [

        "You are carrying:"

    ]

    for item in session.player.inventory:

        lines.append(

            f" - {item.name}"

        )

    return "\r\n".join(lines)


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
