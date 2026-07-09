import random


def roll(
    sides,
    count=1
):

    results = []

    for _ in range(count):

        results.append(
            random.randint(
                1,
                sides
            )
        )

    return results



def total(
    sides,
    count=1
):

    return sum(
        roll(
            sides,
            count
        )
    )



def ability_check(
    modifier=0
):

    return roll(
        20
    )[0] + modifier
