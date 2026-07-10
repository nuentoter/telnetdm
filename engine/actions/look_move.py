from engine.action_handler import action
from engine.encounter import check_encounter
from engine.combat import Combat



def describe_room(room):

    lines = [

        room["name"],

        room["description"]

    ]


    if room.get("exits"):

        lines.append(

            "Exits: "

            + ", ".join(
                room["exits"].keys()
            )

        )


    if room.get("items"):

        lines.append(

            "You see:"

        )


        for item in room["items"]:

            lines.append(

                f" - {item.name}"

            )


    return "\r\n".join(lines)



@action("look")
def do_look(

    session,

    action,

    world

):

    room = world.get_room(

        session.player.room

    )


    return describe_room(room)



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


    result = describe_room(room)


    encounter = check_encounter(

        room["id"]

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
