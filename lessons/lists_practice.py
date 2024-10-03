"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor
# print(my_numbers)

# String Analogy
# my_name: str = "" # literal
# my_name: str = str() # constructor


# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)


# Creating an already ppoulated list
game_points: list[int] = [102, 86, 94]
print(game_points)


# Subscription/ Notation indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)


# Modifying by index
# (Beacause lists are mutable)
game_points[1] = 72
print(game_points)


# class_num: str = "110"  # chnage it to "210"
# class_num[0] = 2
# Can't modify strings by index


# Getting the length
# print(len(game_points))


# Removing an item
game_points.pop(1)
print(game_points)


# Function name: display
# Parameter: list of integers
# RV: none
# Print: every element in the input list
# Call display on game_points

# def display (int_list: )
