from engine.world import WORLD
from engine.dice import d2, d4, d6, d8, d10, d12, d20, d100


def handle_command(session, cmd: str):
    cmd = cmd.strip().lower()

    if cmd in ("look", "l"):
        room = WORLD[session.player.room]
        session.send(f"\n{room['name']}")
        session.send(room["description"])
        session.send(f"Exits: {', '.join(room['exits'].keys())}")
        return

    if cmd.startswith("go "):
        direction = cmd.split(" ", 1)[1]
        room = WORLD[session.player.room]

        if direction in room["exits"]:
            session.player.room = room["exits"][direction]
            # auto-look after moving
            return handle_command(session, "look")
        else:
            session.send("You cannot go that way.")
        return

        if cmd.startswith("roll"):
        parts = cmd.split()

        if len(parts) == 1:
            result = d20()
            session.send(f"You roll a d20: {result}")
            return

        die = parts[1]

        dice_map = {
            "d2": d2,
            "d4": d4,
            "d6": d6,
            "d8": d8,
            "d10": d10,
            "d12": d12,
            "d20": d20,
            "d100": d100,
        }

        if die in dice_map:
            result = dice_map[die]()
            session.send(f"You roll {die}: {result}")
            return

        session.send("Unknown die. Use d2, d4, d6, d8, d10, d12, d20, d100")
        return
    
    if cmd in ("quit", "exit"):
        session.send("Farewell, adventurer.")
        return "quit"

    session.send("Unknown command.")
