from engine.resolver import resolve_item
from engine.world import WORLD


def execute_action(session, action):

    if action.type == "look":
        room = WORLD[session.player.room]
        return describe_room(room)

    if action.type == "move":
        return move_player(session, action.target)

    if action.type == "take":
        return take_item(session, action.target)

    return "You are unsure what you want to do."


def describe_room(room):

    return room.describe()


def move_player(session, direction):

    room = WORLD[session.player.room]

    if direction not in room.exits:
        return "You cannot go that way."

    session.player.room = room.exits[direction]

    new_room = WORLD[session.player.room]

    return describe_room(new_room)


def take_item(session, target):

    room = WORLD[session.player.room]

    item = resolve_item(
        target,
        room.items
    )

    if not item:
        return "You don't see anything like that here."

    room.items.remove(item)

    session.player.add_item(item)

    return f"You take the {item}."
