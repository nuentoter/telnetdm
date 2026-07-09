from engine.player import Player
from engine.player_storage import load_player, apply_saved_player


class Session:


    def __init__(
        self,
        writer
    ):

        self.writer = writer

        self.player = Player()


        saved = load_player()


        if saved:

            apply_saved_player(

                self.player,

                saved

            )



    def send(
        self,
        text
    ):

        self.writer.write(
            text + "\r\n"
        )
