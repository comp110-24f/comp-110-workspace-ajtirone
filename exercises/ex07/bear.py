"""File to define Bear class."""

__author__ = "730676761"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        # Initializing age and hunger_score
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        self.age += 1  # Increase bear's age by 1
        self.hunger_score -= 1  # Decrease hunger score by 1 each day
        return None

    def eat(self, num_fish: int):
        # Increase the hunger_score by the number of fish eaten
        self.hunger_score += num_fish
        return None
