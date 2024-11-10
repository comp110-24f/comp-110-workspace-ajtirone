"""File to define River class."""

__author__ = "730676761"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        # Create a new list for surviving fish (age 3 or less)
        surviving_fish = []
        for fish in self.fish:  # Loop through every fish in river
            if fish.age <= 3:
                surviving_fish.append(fish)
                # Copy over only the fish that should survive
                # If the fish's age is > 3 it is removed from fish
        self.fish = surviving_fish  # Updating self.fish to be equal to copied list

        # Create a new list for surviving bears (age 5 or less)
        surviving_bears = []
        for bear in self.bears:  # Loop through every bear in river
            if bear.age <= 5:
                surviving_bears.append(bear)
                # Copy over only the bears that should survive
                # If the bears age is > 5 it is removed from fish
        self.bears = surviving_bears  # Updating self.bears to be equal to copied list
        return None

    def remove_fish(self, amount: int):
        # Remove the specified number of fish from the front of the list
        removed = 0
        while removed < amount and self.fish:
            # loop to ensure that we remove up to amount fish
            # and self.fish makes sure there are still fish to remove
            self.fish.pop(0)  # Remove fish at front
            removed += 1
        return None

    def bears_eating(self):
        if len(self.fish) >= 5:  # Makes sure there are at least 5 fish in river
            # Each bear will eat 3 fish
            for bear in self.bears:  # Loop through every bear in river
                self.remove_fish(3)  # Remove 3 fish from river
                bear.eat(3)  # Calling eat for the num of fish bear eats
                # Bear eats 3 fish
        return None

    def check_hunger(self):
        surviving_bears = []  # Creating new list to store surviving bears
        for bear in self.bears:  # Loop through every bear in river
            if bear.hunger_score > 0:
                surviving_bears.append(bear)
                # If the bear isn't starving add it to new list
                # Any bear with a hunger score < 0 is removed from the river
        self.bears = surviving_bears  # Updating self.bears to be equal to copied list
        return None

    def repopulate_fish(self):
        new_fish = (len(self.fish) // 2) * 4
        # Each pair of fish will produce 4 offspring
        count = 0  # Counter to track new fish
        while count < new_fish:  # Create new fish until target count reached
            self.fish.append(Fish())  # Add new fish to river's fish population
            count += 1  # Increase the count by 1 for every new fish
        return None

    def repopulate_bears(self):
        new_bears = len(self.bears) // 2
        # Each pair of Bear’s will produce 1 offspring
        count = 0  # Counter to track new bears
        while count < new_bears:  # Create new bears until target count reached
            self.bears.append(Bear())  # Add new bears to river's bear population
            count += 1  # Increase the count by 1 for every new bear
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        days = 0  # Initialize counter for days
        while days < 7:  # Calls one_river_day 7 times
            self.one_river_day()
            days += 1  # Increment counter by 1 each time
