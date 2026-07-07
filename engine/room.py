class Room:

    def __init__(
        self,
        room_id,
        name,
        description,
        exits=None,
        items=None,
        npcs=None,
        hidden=None,
    ):

        self.id = room_id

        self.name = name

        self.description = description

        self.exits = exits or {}

        self.items = items or []

        self.npcs = npcs or []

        self.hidden = hidden or {}



    def describe(self):

        lines = []


        lines.append(self.name)

        lines.append(self.description)


        if self.exits:

            lines.append(
                "Exits: "
                +
                ", ".join(
                    self.exits.keys()
                )
            )


        if self.items:

            lines.append("")

            lines.append(
                "You see:"
            )

            for item in self.items:

                lines.append(
                    f" - {item}"
                )


        if self.npcs:

            lines.append("")

            lines.append(
                "People here:"
            )

            for npc in self.npcs:

                lines.append(
                    f" - {npc}"
                )


        return "\r\n".join(lines)
