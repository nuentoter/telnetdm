from engine.parser import Parser
from engine.dispatcher import Dispatcher

from engine.intent import parse_input
from engine.action_definitions import intent_to_action
from engine.action_handler import execute_action

from engine.world_manager import WorldManager
from engine.registry import Registry


class Game:

    def __init__(self):

        self.sessions = {}

        self.registry = Registry()

        self.world = WorldManager(
            self.registry
        )

        self.parser = Parser()

        self.dispatcher = Dispatcher(
            execute_action
        )



    def connect(
        self,
        session
    ):

        self.sessions[
            id(session)
        ] = session



    def disconnect(
        self,
        session
    ):

        self.sessions.pop(
            id(session),
            None
        )



    def process_command(

        self,

        session,

        command

    ):

        intent = self.parser.parse(
            command
        )


        if intent.action == "system":

            if intent.target in [

                "quit",
                "exit",
                "logout"

            ]:

                return "quit"



        action = intent_to_action(
            intent
        )


        print(
            "DEBUG ACTION:",
            action
        )


        return self.dispatcher.dispatch(

            session,

            action,

            self.world

        )
