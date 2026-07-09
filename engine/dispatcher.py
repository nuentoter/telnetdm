class Dispatcher:

    def __init__(

        self,

        handler

    ):

        self.handler = handler



    def dispatch(

        self,

        session,

        action,

        world

    ):

        return self.handler(

            session,

            action,

            world

        )
