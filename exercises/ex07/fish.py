"""File to define Fish class."""

__author__ = "730676761"


class Fish:
    age: int

    def __init__(self):
        self.age: int = 0  # Initializing age
        return None

    def one_day(self):
        self.age += 1  # Increase fish's age by 1
        return None
