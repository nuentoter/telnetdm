class Item:

    def __init__(
        self,
        item_id,
        name,
        aliases=None,
        description="",
        weight=0.0,
        value=0,
        portable=True,
    ):

        self.id = item_id

        self.name = name

        self.aliases = aliases or []

        self.description = description

        self.weight = weight

        self.value = value

        self.portable = portable


    def matches(self, text):

        text = text.lower()

        if text == self.name.lower():
            return True

        for alias in self.aliases:
            if text == alias.lower():
                return True

        return False


    def __str__(self):
        return self.name
