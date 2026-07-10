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

        if text == direction:

            return Intent(

                "move",

                direction,

                0.95

            )



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



    if text.startswith(

        (

            "unequip ",

            "remove ",

            "take off "

        )

    ):

        cleaned = remove_words(

            text,

            [

                "unequip",

                "remove",

                "take",

                "off"

            ]

        )


        return Intent(

            "unequip",

            clean_target(cleaned),

            0.9

        )



    if text.startswith(

        (

            "attack",

            "hit",

            "strike",

            "fight"

        )

    ):

        cleaned = remove_words(

            text,

            [

                "attack",

                "hit",

                "strike",

                "fight"

            ]

        )


        return Intent(

            "attack",

            clean_target(cleaned),

            0.9

        )



    if text.startswith(

        (

            "inspect",

            "examine"

        )

    ):

        cleaned = remove_words(

            text,

            [

                "inspect",

                "examine"

            ]

        )


        return Intent(

            "enemy",

            clean_target(cleaned),

            0.85

        )



    if text.startswith(

        (

            "inventory",

            "inv",

            "items",

            "belongings"

        )

    ):

        return Intent(

            "inventory",

            None,

            0.95

        )



    if text.startswith(

        (

            "look",

            "see",

            "observe",

            "check"

        )

    ):

        return Intent(

            "look",

            None,

            0.9

        )



    if text.startswith(

        (

            "take",

            "grab",

            "get",

            "pick"

        )

    ):

        cleaned = remove_words(

            text,

            [

                "take",

                "grab",

                "get",

                "pick",

                "up"

            ]

        )


        return Intent(

            "take",

            clean_target(cleaned),

            0.85

        )



    return Intent(

        "unknown",

        text,

        0.2

    )
