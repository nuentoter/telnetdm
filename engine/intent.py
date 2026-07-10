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
        "at",
        "on",
        "into",
        "from"

    ]

    words = text.split()

    words = [

        word

        for word in words

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

        if (

            text == direction

            or

            text.startswith(

                "go " + direction

            )

            or

            text.startswith(

                "walk " + direction

            )

            or

            text.startswith(

                "move " + direction

            )

        ):

            return Intent(

                action="move",

                target=direction,

                confidence=0.95

            )


    if any(

        word in text

        for word in [

            "equipment",

            "gear"

        ]

    ):

        return Intent(

            action="equipment",

            confidence=0.95

        )


    if any(

        word in text

        for word in [

            "inventory",

            "inv",

            "items",

            "carrying",

            "bag",

            "backpack"

        ]

    ):

        return Intent(

            action="inventory",

            confidence=0.95

        )


    if any(

        word in text

        for word in [

            "equip",

            "wear",

            "wield"

        ]

    ):

        cleaned = remove_words(

            text,

            [

                "equip",

                "wear",

                "wield"

            ]

        )

        return Intent(

            action="equip",

            target=clean_target(

                cleaned

            ),

            confidence=0.95

        )


    if any(

        word in text

        for word in [

            "unequip",

            "remove",

            "take off"

        ]

    ):

        cleaned = remove_words(

            text,

            [

                "unequip",

                "remove",

                "take off"

            ]

        )

        return Intent(

            action="unequip",

            target=clean_target(

                cleaned

            ),

            confidence=0.95

        )


    if any(

        word in text

        for word in [

            "look",

            "see",

            "inspect",

            "observe",

            "examine"

        ]

    ):

        return Intent(

            action="look",

            confidence=0.90

        )


    if any(

        word in text

        for word in [

            "attack",

            "fight",

            "hit",

            "strike",

            "slash",

            "stab",

            "kill"

        ]

    ):

        cleaned = remove_words(

            text,

            [

                "attack",

                "fight",

                "hit",

                "strike",

                "slash",

                "stab",

                "kill"

            ]

        )

        return Intent(

            action="attack",

            target=clean_target(

                cleaned

            ),

            confidence=0.95

        )


    if any(

        word in text

        for word in [

            "enemy",

            "inspect enemy",

            "inspect wolf",

            "examine wolf"

        ]

    ):

        return Intent(

            action="enemy",

            confidence=0.90

        )


    if any(

        word in text

        for word in [

            "flee",

            "run",

            "escape"

        ]

    ):

        return Intent(

            action="flee",

            confidence=0.90

        )


    if any(

        word in text

        for word in [

            "take",

            "grab",

            "pick",

            "get",

            "collect",

            "loot"

        ]

    ):

        cleaned = remove_words(

            text,

            [

                "take",

                "grab",

                "pick",

                "up",

                "get",

                "collect",

                "loot"

            ]

        )

        return Intent(

            action="take",

            target=clean_target(

                cleaned

            ),

            confidence=0.90

        )


    if any(

        word in text

        for word in [

            "drop",

            "discard",

            "leave"

        ]

    ):

        cleaned = remove_words(

            text,

            [

                "drop",

                "discard",

                "leave"

            ]

        )

        return Intent(

            action="drop",

            target=clean_target(

                cleaned

            ),

            confidence=0.90

        )


    if any(

        word in text

        for word in [

            "talk",

            "speak",

            "ask",

            "hello",

            "greet"

        ]

    ):

        cleaned = remove_words(

            text,

            [

                "talk",

                "speak",

                "ask",

                "hello",

                "greet",

                "say"

            ]

        )

        return Intent(

            action="talk",

            target=clean_target(

                cleaned

            ),

            confidence=0.85

        )


    return Intent(

        action="unknown",

        target=text,

        confidence=0.20

    )
