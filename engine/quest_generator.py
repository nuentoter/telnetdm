import random


class QuestGenerator:

    def __init__(self):
        self.templates = [
            {
                "objective": "defeat",
                "targets": ["Forest Wolf", "Bandit", "Goblin"],
                "titles": ["The Local Threat", "A Dangerous Presence"]
            },
            {
                "objective": "collect",
                "targets": ["herbs", "ancient stones", "lost supplies"],
                "titles": ["A Needed Supply", "Gather What Was Lost"]
            }
        ]


    def generate(self, npc=None, location=None):

        template = random.choice(self.templates)
        target = random.choice(template["targets"])
        title = random.choice(template["titles"])

        personality = ""
        if npc:
            personality = getattr(npc, "personality", "")

        return {
            "name": title,
            "description": self.create_description(
                target,
                location,
                personality
            ),
            "objective": template["objective"],
            "target": target,
            "amount": random.randint(1, 5),
            "reward": {
                "xp": random.randint(25, 100),
                "gold": random.randint(5, 50)
            }
        }


    def create_description(self, target, location, personality):

        place = location or "these lands"

        return (
            f"Something troubles {place}. "
            f"A {personality} has asked you to deal with {target}."
        )
