"""Mutating functions."""

__author__ = "730676761"


def manual_append(num_list: list[int], num: int) -> None:
    """Append integer to end of list"""
    num_list.append(num)


def double(num_list: list[int]) -> None:
    """Double every element in the list"""
    idx: int = 0
    while idx < len(num_list):
        num_list[idx] = num_list[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
