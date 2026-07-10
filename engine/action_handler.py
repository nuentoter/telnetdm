ACTION_TABLE = {}


def action(name):

    def decorator(func):

        ACTION_TABLE[name] = func

        return func

    return decorator



def execute_action(

    session,

    action,

    world

):

    func = ACTION_TABLE.get(

        action.type

    )


    if func:

        return func(

            session,

            action,

            world

        )


    return "Nothing happens."



# Load action modules after the registry exists

from engine.actions.look_move import *
from engine.actions.inventory import *
from engine.actions.equipment import *
from engine.actions.combat_actions import *
from engine.actions.interaction import *
