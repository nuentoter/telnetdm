class Action:
    def __init__(self, action_type, target=None):
        self.type = action_type
        self.target = target

    def __repr__(self):
        return (
            f"Action("
            f"type={self.type}, "
            f"target={self.target}"
            f")"
        )


def intent_to_action(intent):
    """
    Converts an Intent object into a game Action.
    """

    return Action(
        action_type=intent.action,
        target=intent.target
    )
