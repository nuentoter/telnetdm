from engine.action_handler import action



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

        return "\r\n".join(lines)



    lines.append(

        "You are carrying:"

    )


    for item in session.player.inventory:

        lines.append(

            f" - {item.name}"

        )


    return "\r\n".join(lines)



@action("drop")
def do_drop(

    session,

    action,

    world

):

    from engine.resolver import resolve_item


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
