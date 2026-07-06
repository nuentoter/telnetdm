import random


def d20():
    return random.randint(1, 20)


def roll(sides: int):
    return random.randint(1, sides)
