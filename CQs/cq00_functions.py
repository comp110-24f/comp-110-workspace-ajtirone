"""Functions Challenge Question"""

__author__ = "730676761"


def mimic(message: str) -> str:
    """Return message back to me"""
    return message


def main() -> None:
    """Print result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
