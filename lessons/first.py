def get_first(input: list[int]) -> int:
    """Return the first element (index 0) of the input list."""
    # assert len(input) > 0
    if len(input) == 0:
        return -1
    return input[0]


def remove_first(input: list[int]) -> None:
    """Remove the first element (index 0) of the input list."""
    if len(input) > 0:
        input.pop(0)


def remove_and_get_first(input: list[int]) -> int:
    """Remove AND return the first element (index 0) of the input list."""
    first: int = input[0]
    input.pop(0)
    return first
