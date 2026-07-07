from engine.intent import parse_input


tests = [
    "go north",
    "walk south",
    "grab the rusty key",
    "pick up the sword",
    "look around",
    "can i see what is here",
    "dance with the goblin"
]


for text in tests:
    intent = parse_input(text)

    print("----------------")
    print("Input:", text)
    print("Action:", intent.action)
    print("Target:", intent.target)
