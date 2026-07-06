from engine.world import WORLD
from engine.dice import d20
from engine.skills import SKILLS


def handle_command(session, cmd: str):
    cmd = cmd.strip().lower()

    # -------------------------
    # LOOK COMMAND
    # -------------------------
    if cmd in ("look", "l"):
        room = WORLD[session.player.room]
        session.send(f"\n{room['name']}")
        session.send(room["description"])
        session.send(f"Exits: {', '.join(room['exits'].keys())}")
        return

    # -------------------------
    # MOVE COMMAND
    # -------------------------
    if cmd.startswith("go "):
        direction = cmd.split(" ", 1)[1]
        room = WORLD[session.player.room]

        if direction in room["exits"]:
            session.player.room = room["exits"][direction]
            return handle_command(session, "look")
        else:
            session.send("You cannot go that way.")
        return

    # -------------------------
    # ROLL COMMAND
    # -------------------------
    if cmd.startswith("roll"):
        parts = cmd.split()

        if len(parts) == 1:
            result = d20()
            session.send(f"You roll a d20: {result}")
            return

        die = parts[1]

        dice_map = {
            "d2": lambda: 1 if d20() <= 10 else 2,
            "d4": lambda: __import__("random").randint(1, 4),
            "d6": lambda: __import__("random").randint(1, 6),
            "d8": lambda: __import__("random").randint(1, 8),
            "d10": lambda: __import__("random").randint(1, 10),
            "d12": lambda: __import__("random").randint(1, 12),
            "d20": d20,
            "d100": lambda: __import__("random").randint(1, 100),
        }

        if die in dice_map:
            result = dice_map[die]()
            session.send(f"You roll {die}: {result}")
            return

        session.send("Unknown die. Use d2, d4, d6, d8, d10, d12, d20, d100")
        return

    # -------------------------
    # SKILL CHECK COMMAND
    # -------------------------
    if cmd.startswith("check"):
        parts = cmd.split()

        if len(parts) < 2:
            session.send("Usage: check <skill>")
            return

        skill = parts[1]

        if skill not in SKILLS:
            session.send(f"Unknown skill: {skill}")
            return

        roll = d20()

        stat_name = SKILLS[skill]
        stat_value = getattr(session.player, stat_name)

        dc = 10

        modifier = stat_value // 2 - 5
        total = roll + modifier

        session.send(f"\nSkill check: {skill}")
        session.send(f"Roll: {roll}")
        session.send(f"Stat: {stat_name} ({stat_value})")
        session.send(f"Total: {total} vs DC {dc}")

        if total >= dc:
            session.send("Result: SUCCESS")
        else:
            session.send("Result: FAILURE")

        return

    # -------------------------
    # QUIT
    # -------------------------
    if cmd in ("quit", "exit"):
        session.send("Farewell, adventurer.")
        return "quit"

    session.send("Unknown command.")
