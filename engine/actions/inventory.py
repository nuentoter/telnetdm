from engine.action_handler import action
from engine.resolver import resolve_item



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


    return "\r\n".join(

        lines

    )



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


    return (

        f"You take the {item.name}."

    )



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


    return (

        f"You drop the {item.name}."

    )
