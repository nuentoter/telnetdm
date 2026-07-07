from engine.system_actions import is_system_action


class Intent:

    def __init__(
        self,
        action,
        target=None,
        confidence=1.0
    ):
        self.action = action
        self.target = target
        self.confidence = confidence


    def to_dict(self):

        return {
            "action": self.action,
            "target": self.target,
            "confidence": self.confidence
        }



def clean_target(text):

    filler = [
        "the",
        "a",
        "an",
        "that",
        "this",
        "my",
        "to",
        "with",
        "about",
        "at"
    ]

    words = text.split()

    words = [
        word for word in words
        if word not in filler
    ]

    return " ".join(words)



def remove_words(text, words):

    for word in words:

        text = text.replace(
            word,
            ""
        )

    return text.strip()



def parse_input(text):

    text = text.lower().strip()


    if is_system_action(text):

        return Intent(
            action="system",
            target=text,
            confidence=1.0
        )



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



    if any(word in text for word in [
        "look",
        "see",
        "examine",
        "observe",
        "inspect",
        "check"
    ]):

        return Intent(
            action="look",
            confidence=0.9
        )



    if any(word in text for word in [
        "take",
        "grab",
        "get",
        "pick",
        "yoink",
        "snatch",
        "steal",
        "collect",
        "pocket"
    ]):

        cleaned = remove_words(
            text,
            [
                "take",
                "grab",
                "get",
                "pick",
                "up",
                "yoink",
                "snatch",
                "steal",
                "collect",
                "pocket"
            ]
        )


        return Intent(
            action="take",
            target=clean_target(cleaned),
            confidence=0.85
        )



    if any(word in text for word in [
        "talk",
        "speak",
        "ask",
        "greet",
        "hello",
        "chat",
        "conversation"
    ]):

        cleaned = remove_words(
            text,
            [
                "talk",
                "speak",
                "ask",
                "greet",
                "hello",
                "chat",
                "conversation",
                "say"
            ]
        )


        return Intent(
            action="talk",
            target=clean_target(cleaned),
            confidence=0.8
        )



    return Intent(
        action="unknown",
        target=text,
        confidence=0.2
    )
