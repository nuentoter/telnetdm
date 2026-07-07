class Intent:
    def __init__(self, action=None, target=None):
        self.action = action
        self.target = target


def parse_input(text):
    """
    Converts natural player language into a simple intent.
    """

    text = text.lower().strip()

    # movement examples
    if any(word in text for word in ["north", "south", "east", "west"]):
        for direction in ["north", "south", "east", "west"]:
            if direction in text:
                return Intent(
                    action="move",
                    target=direction
                )

    # taking objects
    if any(word in text for word in [
        "take",
        "grab",
        "pick up",
        "get"
    ]):
        words = text.split()

        return Intent(
            action="take",
            target=" ".join(words[1:])
        )

    # looking
    if any(word in text for word in [
        "look",
        "see",
        "examine"
    ]):
        return Intent(
            action="look"
        )

    return Intent(
        action="unknown",
        target=text
    )
