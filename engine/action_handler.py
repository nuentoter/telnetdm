from engine.resolver import resolve_item
from engine.world import WORLD
from engine.npc_resolver import resolve_npc


def execute_action(session, action):

    if action.type == "look":

        room = WORLD[
            session.player.room
        ]

        return describe_room(room)



    if action.type == "move":

        return move_player(
            session,
            action.target
        )



    if action.type == "take":

        return take_item(
            session,
            action.target
        )



    if action.type == "talk":

        return talk_to_npc(
            session,
            action.target
        )

    if action.type == "inventory":

        return show_inventory(
            session
        )

    

    return (
        "You are unsure what you want to do."
    )



def describe_room(room):

    return room.describe()



def move_player(session, direction):

    room = WORLD[
        session.player.room
    ]


    if direction not in room.exits:

        return (
            "You cannot go that way."
        )


    session.player.room = (
        room.exits[direction]
    )


    new_room = WORLD[
        session.player.room
    ]


    return describe_room(
        new_room
    )



def take_item(session, target):

    room = WORLD[
        session.player.room
    ]


    item = resolve_item(
        target,
        room.items
    )


    if not item:

        return (
            "You don't see "
            "anything like that here."
        )


    room.items.remove(item)


    session.player.add_item(
        item
    )


    return (
        f"You take the {item.name}."
    )



def talk_to_npc(session, target):

    room = WORLD[
        session.player.room
    ]


    npc = resolve_npc(
        target,
        room.npcs
    )


    if not npc:

        return (
            "You don't see anyone "
            "by that name here."
        )


    return npc.speak()


    return (
        "You don't see anyone "
        "by that name here."
    )
    
def show_inventory(session):

    inventory = session.player.inventory


    if not inventory:

        return (
            "You are carrying nothing."
        )


    lines = [

        "You are carrying:"

    ]


    for item in inventory:

        lines.append(
            f" - {item.name}"
        )


    return "\r\n".join(lines)
