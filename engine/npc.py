class NPC:

    def __init__(
        self,
        npc_id,
        name,
        personality="neutral",
        dialogue=None,
        quests=None
    ):

        self.id = npc_id
        self.name = name
        self.personality = personality
        self.dialogue = dialogue or [
            "The NPC has nothing to say."
        ]
        self.quests = quests or []


    def talk(self):

        if self.quests:

            quest = self.quests[0]

            if hasattr(quest, "description"):

                return (
                    f"{self.name}:\r\n"
                    f"\"{quest.description}\"\r\n"
                    f"Quest offered: {quest.name}"
                )

            return (
                f"{self.name}:\r\n"
                f"\"{quest['description']}\"\r\n"
                f"Quest offered: {quest['name']}"
            )

        return (
            f"{self.name}:\r\n"
            f"\"{self.dialogue[0]}\""
        )


    def add_quest(
        self,
        quest
    ):

        self.quests.append(
            quest
        )


    def describe(self):

        return {
            "id": self.id,
            "name": self.name,
            "personality": self.personality,
            "quests": [
                q.describe() if hasattr(q, "describe") else q
                for q in self.quests
            ]
        }
