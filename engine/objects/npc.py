class NPC:

    def __init__(
        self,
        npc_id,
        name,
        description,
        dialogue=None,
    ):

        self.id = npc_id

        self.name = name

        self.description = description

        self.dialogue = dialogue or []

        self.inventory = []


        # Future AI fields

        self.memory = []

        self.goals = []


    def speak(self):

        if self.dialogue:

            return self.dialogue[0]

        return (
            f"{self.name} has nothing to say."
        )


    def remember(self, event):

        self.memory.append(event)


    def __str__(self):

        return self.name
