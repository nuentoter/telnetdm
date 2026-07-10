class Item(Entity):

    def __init__(

        self,

        item_id,

        name,

        aliases,

        description,

        item_type="misc",

        slot=None,

        damage=0,

        armor=0,

        weight=0,

        value=0

    ):

        super().__init__(
            item_id,
            name
        )

        self.aliases = aliases

        self.description = description

        self.item_type = item_type

        self.slot = slot

        self.damage = damage

        self.armor = armor

        self.weight = weight

        self.value = value
