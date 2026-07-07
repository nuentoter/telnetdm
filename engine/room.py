class Room:

    def __init__(
        self,
        room_id,
        name,
        description,
        exits=None,
        items=None,
        hidden=None,
        npcs=None
    ):

        self.id = room_id

        self.name = name

        self.description = description

        self.exits = exits or {}

        self.items = items or []

        self.hidden = hidden or {}

        self.npcs = npcs or []



        for item in self.items:

            item.location = self.id



    def add_item(self, item):

        item.location = self.id

        self.items.append(
            item
        )



    def remove_item(self, item):

        if item in self.items:

            self.items.remove(
                item
            )

            item.location = None

            return True


        return False



    def describe(self):

        output = []


        output.append(
            self.name
        )


        output.append(
            self.description
        )


        if self.exits:

            output.append(
                "Exits: "
                +
                ", ".join(
                    self.exits.keys()
                )
            )


        if self.items:

            output.append(
                "You see:"
            )


            for item in self.items:

                output.append(
                    f" - {item.name}"
                )


        return "\r\n".join(output)
