import uuid


class Quest:

    def __init__(
        self,
        name,
        description,
        objective,
        target,
        amount=1,
        reward=None
    ):

        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.objective = objective
        self.target = target
        self.amount = amount
        self.progress = 0
        self.completed = False
        self.reward = reward or {
            "xp": 25,
            "gold": 10
        }


    def advance(
        self,
        target
    ):

        if self.completed:
            return

        if target != self.target:
            return

        self.progress += 1

        if self.progress >= self.amount:
            self.completed = True


    def describe(self):

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "objective": self.objective,
            "target": self.target,
            "amount": self.amount,
            "progress": self.progress,
            "completed": self.completed,
            "reward": self.reward
        }


class QuestGenerator:

    @staticmethod
    def generate_kill_quest(target):

        return Quest(
            name=f"The {target} Problem",
            description=f"Remove the threat of {target} from the area.",
            objective="defeat",
            target=target,
            amount=1,
            reward={
                "xp": 50,
                "gold": 25
            }
        )
