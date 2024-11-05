__author__ = "730676761"


from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_expected_value_use_case() -> None:
    """Use case to test that find_and_remove_max returns the expected largest value."""
    a: list[int] = [4, 3, 5, 2, 7]
    find_and_remove_max(a)
    assert a == [4, 3, 5, 2]
    # assert find_and_remove_max([4,3,5,2,7]) == 7


def test_find_and_remove_max_mutation_use_case() -> None:
    """Use case to test that find_and_remove_max correctly mutates input list."""
    b: list[int] = [8, 12, 12, 1, 6]
    find_and_remove_max(b)
    assert b == [8, 1, 6]
    # assert find_and_remove_max([8, 12, 12, 1]) == 12


def test_find_and_remove_max_unconventional_input_edge_case() -> None:
    """Edge case to test that find_and_remove_max returns -1 for empty list."""
    assert find_and_remove_max([]) == -1
