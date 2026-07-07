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
        return handle_command(session, command)
