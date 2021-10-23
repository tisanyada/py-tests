import random


def dice():
    return f"{random.randint(0, 6)},{random.randint(0, 6)}"


print(dice())
