class Item:

    def __init__(

        self,

        item_id,

        name,

        aliases=None,

        description="",

        item_type="misc",

        slot=None,

        damage=0,

        armor=0,

        weight=0,

        value=0

    ):

        self.id = item_id

        self.name = name

        self.aliases = aliases or []

        self.description = description

        self.item_type = item_type

        self.slot = slot

        self.damage = damage

        self.armor = armor

        self.weight = weight

        self.value = value



    def matches(

        self,

        text

    ):

        text = text.lower()

        return (

            text == self.name.lower()

            or

            text == self.id.lower()

            or

            text in [

                alias.lower()

                for alias in self.aliases

            ]

        )



    def describe(self):

        return self.description
