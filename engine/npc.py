from engine.quest_generator import QuestGenerator
import uuid


class NPC:

    def __init__(self, npc_id, name, personality="neutral", dialogue=None, quests=None, database=None):
        self.id = npc_id
        self.name = name
        self.personality = personality
        self.dialogue = dialogue or ["The NPC has nothing to say."]
        self.quests = quests or []
        self.database = database
        self.quest_generator = QuestGenerator()


    def talk(self):

        if not self.quests:
            quest = self.quest_generator.generate(self, self.name)
            quest_id = "quest_" + str(uuid.uuid4())[:8]

            self.quests.append(quest)

            if self.database:
                self.database.add_quest(
                    quest_id,
                    quest
                )

                self.database.add_npc(
                    self.id,
                    self.describe()
                )

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


    def add_quest(self, quest):
        self.quests.append(quest)


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
