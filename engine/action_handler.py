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


@action("attack")
def do_attack(

    session,

    action,

    world

):

    if not hasattr(
        session,
        "combat"
    ):

        return "There is nothing to attack."


    result = session.combat.player_attack()


    if session.combat.finished():

        enemy = session.combat.enemy

        session.player.gain_xp(
            enemy.xp_reward
        )


        session.combat = None


        return (

            f"You defeat the {enemy.name}!\r\n"

            f"You gain {enemy.xp_reward} XP."

        )


    enemy_result = session.combat.enemy_attack()


    return (

        f"You deal {result['damage']} damage.\r\n"

        f"Enemy HP: {result['enemy_hp']}\r\n"

        f"The enemy hits you for {enemy_result['damage']} damage."

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
