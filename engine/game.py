from engine.commands import handle_command
from engine.intent import parse_input
from engine.actions import intent_to_action
from engine.resolver import resolve_item



class Game:

    def __init__(self):
        self.sessions = {}



    def connect(self, session):
        self.sessions[id(session)] = session



    def disconnect(self, session):
        self.sessions.pop(id(session), None)



    def process_command(self, session, command):

        intent = parse_input(command)

        print(
            "DEBUG INTENT:",
            intent.to_dict()
        )


        if intent.action == "system":

            if intent.target in [
                "quit",
                "exit",
                "logout"
            ]:
                return "quit"


        action = intent_to_action(intent)


        print(
            "DEBUG ACTION:",
            action
        )


        if action.type == "move":

            return handle_command(
                session,
                f"go {action.target}"
            )


        if action.type == "look":

            return handle_command(
                session,
                "look"
            )


        if action.type == "take":

            from engine.world import WORLD

            room = WORLD[
                session.player.room
            ]


            item = resolve_item(
                action.target,
                room.get(
                    "items",
                    []
                )
            )


            if item:

                return handle_command(
                    session,
                    f"take {item}"
                )


            return (
                "You don't see anything "
                "like that here."
            )



        return handle_command(
            session,
            command
        )
