"""EX02 - Chardle - Small steps toward wordle"""

__author__ = "730676761"


def input_word() -> str:
    """Ask user to eneter 5 character word and verify length is 5"""
    users_word: str = input("Enter a 5-character word: ")
    if len(users_word) != 5:
        # for the if condition to be true the guess word could be more/less than 5
        # check the length of the word to make sure it has 5 characters
        print("Error: Word must contain 5 characters.")
        exit()  # exit program if word length is not 5 characters
    return users_word


def input_letter() -> str:
    """Ask user to enter a single character"""
    users_letter: str = input("Enter a single character: ")
    if len(users_letter) != 1:
        # check the users input letter to make sure it is 1 character
        print("Error: Character must be a single character.")
        exit()  # exit program if letter is not 1 character
    return users_letter


def contains_char(word: str, letter: str) -> None:
    """Check if input character matches characters in input word"""
    print("Searching for " + letter + " in " + word)

    count: int = 0  # counter to track num of times letter appears in guessed word

    if word[0] == letter:
        # checking whether the first letter of the word is equal to guessed letter
        print(letter + " found at index 0")
        count += 1  # increase the count by 1 if the letter is found at the index 0
    if word[1] == letter:
        # checking whether the second letter of the word is equal to guessed letter
        print(letter + " found at index 1")
        count += 1  # increase the count by 1 if the letter is found at the index 1
    if word[2] == letter:
        # checking whether the thrid letter of the word is equal to the guessed letter
        print(letter + " found at index 2")
        count += 1  # increase the count by 1 if the letter is found at the index 2
    if word[3] == letter:
        # checking whether the fourth letter of the word is equal to the guessed letter
        print(letter + " found at index 3")
        count += 1  # increase the count by 1 if the letter is found at the index 3
    if word[4] == letter:
        # checking whether the fifth letter of the word is equal to the guessed letter
        print(letter + " found at index 4")
        # checks up to 5 indices since wordle will only have 5 characters in guess
        count += 1  # increase the count by 1 if the letter is found at the index 4

    # based on count of instances of the letter in the word print the correct message
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
        # count is anything other than 0 or 1
        # count number will be printed as a concatenated str


def main() -> None:
    """Run Chardle game by calling necessary functions"""
    word: str = input_word()
    letter: str = input_letter()
    contains_char(word, letter)
    # call contains_char function to check for matches in both word and letter


if __name__ == "__main__":
    main()
