class Session:
    def __init__(self, writer):
        self.writer = writer
        self.name = "Wanderer"
        self.room = "start_room"

    def send(self, text: str):
        self.writer.write(text + "\n")
