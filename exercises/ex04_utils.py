"""Apply algorithms for computational thinking practice"""

__author__ = "730676761"


def all(input: list[int], given_int: int) -> bool:
    """Return True if all numbers in the list match the given int, otherwise False."""
    if len(input) == 0:  # means that the list is empty
        return False  # if list is empty, automatically false
    for num in input:
        if num != given_int:  # checks that current num is not equal to the given num
            return False  # when num does not match, return False
    return True
    # if there is no mismatch, the loop is compete, and all nums equal the given num


def max(input: list[int]) -> int:
    """Return the largest number from the list. If list is empty, raise ValueError."""
    if len(input) == 0:  # if list is empty, raise a value error
        raise ValueError("max() arg is an empty List")
    max_num = input[0]  # checks the largest_num with the 1st num in list
    for num in input:  # checks through each num in input to find the max num
        if num > max_num:
            max_num = num  # update max_num value if current num is greater than max_num
    return max_num  # this will be the largest number in the list


def is_equal(input_a: list[int], input_b: list[int]) -> bool:
    """Return True if every num at every idx is equal in both lists, otherwise False"""
    if len(input_a) != len(input_b):
        # see whether the length of 2 lists are different
        return False  # to be equal, they can't be different, so return False
    for index in range(len(input_a)):
        # loop through the index up to the length of the list
        if input_a[index] != input_b[index]:
            return False  # return false if any number is different
    return True  # all elements are same (deep equality)


def extend(input_a: list[int], input_b: list[int]) -> None:
    """Mutate input_a values by appending input_b values to the end."""
    for num in input_b:  # loop through each number in the 2nd list (input_b)
        input_a.append(num)
    # No return statement is needed since the function modifies input_a directly
