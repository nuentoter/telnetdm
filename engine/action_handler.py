from engine.resolver import resolve_item
from engine.npc_resolver import resolve_npc



def execute_action(session, action, world):


    if action.type == "look":

        room = world.get_room(
            session.player.room
        )

        return describe_room(
            room
        )



    if action.type == "move":

        return move_player(
            session,
            action.target,
            world
        )



    if action.type == "take":

        return take_item(
            session,
            action.target,
            world
        )



    if action.type == "talk":

        return talk_to_npc(
            session,
            action.target,
            world
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



def move_player(session, direction, world):

    success = world.move_player(
        session.player,
        direction
    )


    if not success:

        return (
            "You cannot go that way."
        )


    room = world.get_room(
        session.player.room
    )


    return describe_room(
        room
    )



def take_item(session, target, world):

    room = world.get_room(
        session.player.room
    )


    item = resolve_item(
        target,
        room.items
    )


    if not item:

        return (
            "You don't see "
            "anything like that here."
        )


    world.remove_item(
        session.player.room,
        item
    )


    session.player.add_item(
        item
    )


    return (
        f"You take the {item.name}."
    )



def talk_to_npc(session, target, world):

    room = world.get_room(
        session.player.room
    )


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



def show_inventory(session):

    inventory = session.player.inventory


    if not inventory:

        return (
            "You are carrying nothing."
        )


    output = [
        "You are carrying:"
    ]


    for item in inventory:

        output.append(
            f" - {item.name}"
        )


    return "\r\n".join(output)
