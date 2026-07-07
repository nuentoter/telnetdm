class Item:

    def __init__(
        self,
        item_id,
        name,
        aliases=None,
        description="",
        weight=0,
        value=0
    ):

        self.id = item_id

        self.name = name

        self.aliases = aliases or []

        self.description = description

        self.weight = weight

        self.value = value

        self.location = None



    def matches(self, text):

        text = text.lower()


        if text == self.id.lower():

            return True


        if text == self.name.lower():

            return True


        for alias in self.aliases:

            if text == alias.lower():

                return True


        return False



    def __repr__(self):

        return (
            f"Item("
            f"{self.id}"
            f")"
        )
