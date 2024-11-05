"""Define unit tests for the list utility functions in utils.py"""

__author__ = "730676761"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# Tests for only_evens function
def test_only_evens_all_evens_use_case() -> None:
    """Testing only_evens function returns every element in the list."""
    assert only_evens([4, 6, 32, 68]) == [4, 6, 32, 68]


def test_only_evens_even_and_odd_use_case() -> None:
    """Testing only_evens with a mix of even/odd nums. Only even should be returned."""
    assert only_evens([5, 24, 33, 88, 2, 19, 13, 16]) == [24, 88, 2, 16]


def test_only_evens_no_even_edge_case() -> None:
    """Testing only_evens fucntion with no even nums in list."""
    assert only_evens([3, 9, 35, 13, 7]) == []


# Tests for sub function
def test_sub_within_range_use_case() -> None:
    """Testing sub function returns a sublist within the range."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8], 1, 6) == [2, 3, 4, 5, 6]


def test_sub_end_index_greater_than_list_len_use_case() -> None:
    """Testing sub function ends with the end of list when the end index > list len"""
    assert sub([20, 19, 18, 17, 16], 1, 6) == [19, 18, 17, 16]


def test_sub_negative_start_index_use_case() -> None:
    """Testing sub func with negative start will start from beginning of list, idx 0."""
    assert sub([33, 44, 55, 66, 77], -3, 3) == [33, 44, 55]


def test_sub_end_index_less_than_or_equal_to_0_edge_case() -> None:
    """Testing sub function returns empty list when end is <= 0."""
    assert sub([27, 34, 89, 92, 13, 16], 2, -4) == []


# Tests for add_at_index function
def test_add_at_index_insert_middle_use_case() -> None:
    """Testing add_at_index modifies the input list to place the elem in middle."""
    a: list[int] = [100, 101, 103, 104]
    add_at_index(a, 102, 2)
    assert a == [100, 101, 102, 103, 104]


def test_add_at_index_insert_beginning_use_case() -> None:
    """Testing add_at_index modifies the input list to place the elem at beginning."""
    a: list[int] = [4, 5, 6, 7, 8]
    add_at_index(a, 3, 0)
    assert a == [3, 4, 5, 6, 7, 8]


def test_add_at_index_index_out_of_range_edge_case() -> None:
    """Testing add_at_index rises an IndexError when the index is out of range."""
    with pytest.raises(IndexError):
        add_at_index([33, 44, 55, 66, 77], 88, 6)
