from engine.action_handler import action
from engine.encounter import check_encounter
from engine.combat import Combat



@action("look")
def do_look(

    session,

    action,

    world

):

    return world.get_room(

        session.player.room

    ).describe()



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
