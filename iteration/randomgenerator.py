import random


class RandomNumber:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        randrange(min, max)


def randrange(min, max):
    random_number = random.randint(min, max)
    return random_number
