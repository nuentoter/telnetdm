from engine.commands import handle_command
from engine.intent import parse_input
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

        print("DEBUG INTENT:", intent.to_dict())


        if intent.action == "move":
            return handle_command(
                session,
                f"go {intent.target}"
            )


        if intent.action == "look":
            return handle_command(
                session,
                "look"
            )


        if intent.action == "take":

            from engine.world import WORLD

            room = WORLD[session.player.room]

            item = resolve_item(
                intent.target,
                room.get("items", [])
            )

            if item:
                return handle_command(
                    session,
                    f"take {item}"
                )

            session.send(
                "You don't see anything like that here."
            )

            return


        return handle_command(
            session,
            command
        )
