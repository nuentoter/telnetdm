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



def load_actions():

    import engine.actions.look_move
    import engine.actions.inventory
    import engine.actions.equipment
    import engine.actions.combat_actions
    import engine.actions.interaction



load_actions()
