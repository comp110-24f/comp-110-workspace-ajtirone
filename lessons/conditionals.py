"""Practice with conditionals"""


def less_than_10(num: int) -> bool:
    """Tell me if num is < 10"""
    dub: int = num * 2
    dub = dub - 1
    if num < 10:
        print("Small number")
    else:
        print("Big number")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:
        print("Eat more food silly goose")


def check_first_letter(word: str, letter: str) -> str:
    """Tells me whether first character of a word is a letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
