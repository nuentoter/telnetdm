import random


def roll(sides: int):
    return random.randint(1, sides)


def d2():
    return roll(2)


def d4():
    return roll(4)


def d6():
    return roll(6)


def d8():
    return roll(8)


def d10():
    return roll(10)


def d12():
    return roll(12)


def d20():
    return roll(20)


def d100():
    return roll(100)
