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


def execute_action(session, action, world):

    func = ACTION_TABLE.get(action.type)

    if func:

        return func(session, action, world)

    return "Nothing happens."


@action("look")
def do_look(session, action, world):

    return world.get_room(
        session.player.room
    ).describe()


@action("move")
def do_move(session, action, world):

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


@action("equip")
def do_equip(session, action, world):

    item = resolve_item(
        action.target,
        session.player.inventory
    )

    if not item:

        return "You do not have that item."

    if not getattr(item, "slot", None):

        return "You cannot equip that."

    session.player.equip(item)

    return (
        f"You equip the {item.name}."
    )


@action("unequip")
def do_unequip(session, action, world):

    for slot, item in session.player.equipment.items():

        if item is None:
            continue

        if item.matches(action.target):

            session.player.unequip(slot)

            return (
                f"You remove the {item.name}."
            )

    return "You are not wearing that."


@action("equipment")
def do_equipment(session, action, world):

    weapon = session.player.equipment["weapon"]
    armor = session.player.equipment["armor"]

    lines = [
        "Equipment:",
        f"Weapon: {weapon.name if weapon else 'None'}",
        f"Armor : {armor.name if armor else 'None'}"
    ]

    return "\r\n".join(lines)


# --- KEEP THE REST OF YOUR CURRENT FILE EXACTLY AS IT IS ---
# do_attack()
# do_enemy()
# do_flee()
# do_take()
# do_drop()
# do_inventory()
# do_talk()
