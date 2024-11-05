"""Summing the elements of a list using different loops"""

__author__ = "730676761"


def w_sum(vals: list[float]) -> float:
    if len(vals) == 0:
        return 0.0
    sum_vals = vals[0]
    index = 1
    while index < len(vals):
        sum_vals += vals[index]
        index += 1
    return sum_vals


def f_sum(vals: list[float]) -> float:
    sum_vals = 0.0
    for val in vals:
        sum_vals += val
    return sum_vals


def f_range_sum(vals: list[float]) -> float:
    sum_vals = 0.0
    for index in range(len(vals)):
        sum_vals += vals[index]
    return sum_vals
