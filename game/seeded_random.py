import random


class SeededRandom:
    def __init__(self):
        self.random = random

    def rand_int(self, max_int):
        return self.random.randint(0, max_int)
