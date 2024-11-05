"""Implement list utility functions"""

__author__ = "730676761"


def only_evens(int_list: list[int]) -> list[int]:
    """Return a new list containing only the even elements from the input list"""
    even = []  # Initialize an empty list to store the even numbers
    for int in int_list:  # Go through each int in the input list
        if int % 2 == 0:
            # Check whether the int is even. Any even int should have a remainder mod of 0.
            even.append(int)  # If the int is even add it to the list
    return even  # Return the list of even numbers


def sub(int_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Return a subset of the input list. Must be between the start and end idx"""
    if len(int_list) == 0 or start_index >= len(int_list) or end_index <= 0:
        return []
    # If the list is empty, or the indices are invalid, return or empty list
    if start_index < 0:
        start_index = 0  # Start index should be 0 if it's negative
    if end_index > len(int_list):
        end_index = len(int_list)
        # End index should be length of list if its greater than length of input list

    subset_list = []  # Initialize an empty list to store the subset
    for index in range(start_index, end_index):
        # Go through range from start to end index and create subset
        subset_list.append(int_list[index])  # Add current elem to subset list
    return subset_list  # Return the final subset


def add_at_index(int_list: list[int], int_element: int, given_index: int) -> None:
    """Put element at the given index in the input list. IndexError if our of range"""
    if given_index < 0 or given_index > len(int_list):
        raise IndexError("Index is out of bounds for the input list")
    # If given index is out of range, raise an IndexError
    int_list.append(0)
    # Add a "holder element" at the end of the list to create space for shifting
    for index in range(len(int_list) - 1, given_index, -1):
        # Shift elements to the right, from last element to the given index
        int_list[index] = int_list[index - 1]  # Move the element at indedx-1 to index
    int_list[given_index] = int_element  # Put the new element at the index
