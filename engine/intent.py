class Intent:
    def __init__(self, action, target=None, confidence=1.0):
        self.action = action
        self.target = target
        self.confidence = confidence

    def to_dict(self):
        return {
            "action": self.action,
            "target": self.target,
            "confidence": self.confidence
        }


def parse_input(text):
    """
    Temporary parser.
    Later replaced or assisted by local LLM.
    """

    text = text.lower().strip()

    # movement
    directions = [
        "north",
        "south",
        "east",
        "west"
    ]

    for direction in directions:
        if direction in text:
            return Intent(
                action="move",
                target=direction,
                confidence=0.95
            )

    # looking
    if any(word in text for word in [
        "look",
        "see",
        "examine",
        "observe"
    ]):
        return Intent(
            action="look",
            confidence=0.9
        )

    # taking
    if any(word in text for word in [
        "take",
        "grab",
        "get",
        "pick",
        "yoink",
        "snatch",
        "steal"
    ]):
        cleaned = text

        for word in [
            "take",
            "grab",
            "get",
            "pick",
            "up",
            "yoink",
            "snatch",
            "steal"
        ]:
            cleaned = cleaned.replace(word, "")

        return Intent(
            action="take",
            target=cleaned.strip(),
            confidence=0.85
        )

    return Intent(
        action="unknown",
        target=text,
        confidence=0.2
    )
