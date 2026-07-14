from engine.action_handler import action
from engine.npc_resolver import resolve_npc


@action("talk")
def do_talk(session, action, world):

    room = world.get_room(session.player.room)

    npc = resolve_npc(
        action.target,
        room.npcs
    )

    if not npc:
        return "Nobody by that name is here."

    return npc.talk()


@action("accept")
def do_accept(session, action, world):

    room = world.get_room(session.player.room)

    for npc in room.npcs:

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
