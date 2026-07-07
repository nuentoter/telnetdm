SYSTEM_ACTIONS = [
    "quit",
    "exit",
    "logout",
    "save",
    "help",
    "who"
]


def is_system_action(text):

    text = text.lower().strip()

    return text in SYSTEM_ACTIONS
