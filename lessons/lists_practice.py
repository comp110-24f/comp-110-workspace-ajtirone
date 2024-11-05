"""Basic syntax of lists"""

# Create an empty list of floats with the name my_numbers
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor
# print(my_numbers)

# String Analogy
# my_name: str = "" # literal
# my_name: str = str() # constructor


# Adding a value to a list
# Add the value 1.5 to my_numbers
my_numbers.append(1.5)
# Add the value 2.3 to my_numbers
my_numbers.append(2.3)
# print(my_numbers)


# Creating an already poulated list
# Create a list called game_points that store the following numbers: 102, 86, 94
game_points: list[int] = [102, 86, 94]
print(game_points)


# Subscription/ Notation indexing
# In game_points use subscription notation to print out 94
# print(game_points[2])
last_game: int = game_points[2]  # storing the value 94 as something
# print(last_game)


# Modifying by index
# (Beacause lists are mutable)
# In game_points, use subsciption notation to change 86 to 72
game_points[1] = 72
print(game_points)


# class_num: str = "110"  # chnage it to "210"
# class_num[0] = 2
# Can't modify strings by index


# Getting the length
# Print the length of game_points
print(len(game_points))  # don't need the print its just going to print the value


# Removing an item
# Remove 72 from game_points
game_points.pop(1)
print(game_points)

# Practice Function Writing
# Function name: display
# Parameter: list of integers
# RV: none
# Print: every element in the input list
# Call display on game_points


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""

    index: int = 0

    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
