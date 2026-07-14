from engine.action_handler import action
from engine.npc_resolver import resolve_npc
from engine.npc_factory import create_npcs



def get_room_npcs(room, world):

    npcs = room.get("npcs", []) if isinstance(room, dict) else getattr(room, "npcs", [])

    if npcs and isinstance(npcs[0], dict):
        npcs = create_npcs(
            npcs,
            world.database
        )

        if isinstance(room, dict):
            room["npcs"] = npcs

    return npcs


@action("talk")
def do_talk(session, action, world):

    room = world.get_room(session.player.room)

    npcs = get_room_npcs(room, world)

    npc = resolve_npc(
        action.target,
        npcs
    )

    if not npc:
        return "Nobody by that name is here."

    return npc.talk()


@action("accept")
def do_accept(session, action, world):

    room = world.get_room(session.player.room)

    for npc in get_room_npcs(room, world):

        if npc.quests:

            quest = npc.quests[0]
            session.player.add_quest(quest)

            return (
                f"Quest accepted: {quest.name}"
                if hasattr(quest, "name")
                else f"Quest accepted: {quest['name']}"
            )

    return "There are no quests available here."


@action("quests")
def do_quests(session, action, world):

    return session.player.describe_quests()
