from engine.action_handler import action
from engine.npc_resolver import resolve_npc



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

        return (

            "Nobody by that name is here."

        )


    return npc.speak()
