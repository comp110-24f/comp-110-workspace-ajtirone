from lessons.first import get_first, remove_and_get_first, remove_first


def test_get_first_use_case() -> None:
    """Testing get_first function returns the first function in a typical input"""
    assert get_first([4, 5, 6, 7]) == 4


def test_get_first_edge_case() -> None:
    """Testing get_first on empty list"""
    assert get_first([]) == -1


def test_remove_first_use_case() -> None:
    """Testing remove_first removes first element"""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]


def test_remove_first_edge_case() -> None:
    """Testing remove first on empty list. Should not do anything"""
    a: list[int] = []
    remove_first(a)
    assert a == []


def test_remove_and_get_first_return_val_use_case() -> None:
    """Testing remove_and_get_first returns the first element in a typical input"""
    assert remove_and_get_first([4, 5, 6, 7]) == 4


def test_remove_and_get_first_mutation_use_case() -> None:
    """Testing remove_and_get_first removes the first element in a typical input"""
    a: list[int] = [102, 45, 76]
    remove_and_get_first(a)
    assert a == [45, 76]
