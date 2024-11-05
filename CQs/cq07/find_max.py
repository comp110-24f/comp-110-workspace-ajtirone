__author__ = "730676761"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    max_input = max(input)
    while max_input in input:
        input.remove(max_input)
    return max_input
