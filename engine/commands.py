from engine.world import WORLD


def handle_command(session, cmd: str):
    cmd = cmd.strip().lower()

    if cmd in ("look", "l"):
        room = WORLD[session.room]
        session.send(f"\n{room['name']}")
        session.send(room["description"])
        session.send(f"Exits: {', '.join(room['exits'].keys())}")
        return

    if cmd.startswith("go "):
        direction = cmd.split(" ", 1)[1]
        room = WORLD[session.player.room]

        if direction in room["exits"]:
            session.player.room = room["exits"][direction]
            handle_command(session, "look")
        else:
            session.send("You cannot go that way.")
        return

    if cmd in ("quit", "exit"):
        session.send("Farewell, adventurer.")
        return "quit"

    session.send("Unknown command.")
