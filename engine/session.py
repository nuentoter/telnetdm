from engine.player import Player


class Session:
    def __init__(self, writer):
        self.writer = writer
        self.player = Player()

    def send(self, text: str):
        self.writer.write(text + "\r\n")
