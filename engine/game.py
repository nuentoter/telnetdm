from engine.commands import handle_command
from engine.intent import parse_input


class Game:
    def __init__(self):
        self.sessions = {}

    def connect(self, session):
        self.sessions[id(session)] = session

    def disconnect(self, session):
        self.sessions.pop(id(session), None)

    def process_command(self, session, command):

        # First attempt to understand natural language
        intent = parse_input(command)

        # For now, keep the old command system working
        # while we gradually replace it.

        if intent.action == "move":
            command = f"go {intent.target}"

        elif intent.action == "look":
            command = "look"

        elif intent.action == "take":
            command = f"take {intent.target}"

        return handle_command(session, command)
