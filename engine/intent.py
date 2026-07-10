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
            "system",
            text,
            1.0
        )



    directions = [

        "north",
        "south",
        "east",
        "west"

    ]


    for direction in directions:

        if text == direction or text.startswith(direction + " "):

            return Intent(
                "move",
                direction,
                0.95
            )



    # EQUIP MUST COME BEFORE INVENTORY

    if text.startswith(
        (
            "equip ",
            "wear ",
            "wield ",
            "put on "
        )
    ):

        cleaned = remove_words(

            text,

            [

                "equip",
                "wear",
                "wield",
                "put",
                "on"

            ]

        )


        return Intent(

            "equip",

            clean_target(cleaned),

            0.9

        )



    if text in [

        "inventory",
        "inv",
        "items",
        "belongings",
        "carrying",
        "stats",
        "status",
        "character"

    ]:

        return Intent(

            "inventory",

            None,

            0.95

        )



    if any(

        text.startswith(word)

        for word in [

            "look",
            "see",
            "examine",
            "observe",
            "inspect",
            "check"

        ]

    ):

        return Intent(

            "look",

            None,

            0.9

        )



    if any(

        text.startswith(word)

        for word in [

            "take",
            "grab",
            "get",
            "pick",
            "yoink",
            "snatch",
            "steal",
            "collect",
            "pocket"

        ]

    ):

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

            "take",

            clean_target(cleaned),

            0.85

        )



    if any(

        text.startswith(word)

        for word in [

            "attack",
            "hit",
            "strike",
            "fight"

        ]

    ):

        return Intent(

            "attack",

            None,

            0.9

        )



    return Intent(

        "unknown",

        text,

        0.2

    )
