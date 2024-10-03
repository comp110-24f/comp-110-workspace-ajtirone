"""Create a wordle-like game"""

__author__ = "730676761"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user to input a guess, until guess of correct length is provided"""
    guess = input(f"Enter a {secret_word_len} character word: ")
    # Prompt user to enter guess that is the exact length of secret word
    while len(guess) != secret_word_len:
        # Loop until user guesses word with correct length
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess  # Return correct guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Test each index of secret_word to determine whether it matches char_guess"""
    assert len(char_guess) == 1
    # Makes sure that char_guess is only 1 character in length
    index = 0
    while index < len(secret_word):
        # Check each charcter in the secret word, until it is same length as secret word
        if secret_word[index] == char_guess:
            # Check if the current char of the secret word matches the char in the guess
            return True  # If match, then value is true, exit loop
        index += 1  # Increase by 1 to check next character in the secret word
        # Increase by 1 to check the nect character of guess against secret word
    return False  # If no match in character, then return false


def emojified(users_guess: str, secret_word: str) -> str:
    """Compare users_guess and secret_word to display emojis representing result
    of guess"""
    assert len(users_guess) == len(secret_word)
    # Makes sure both the word the user guesses and secret word are same length

    # Unicode characters for the emojis
    white_box: str = "\U00002B1C"  # White square emoji == incorrect guess
    green_box: str = "\U0001F7E9"  # Green square emoji == correct guess
    yellow_box: str = "\U0001F7E8"  # Yellow sqr emoji == correct guess, wrong postion

    emojis: str = ""  # Empty string for emojis results to be displayed
    index = 0  # Index starts at 0, representing first character in word
    while index < len(users_guess):  # Loop through every character in users guess
        if users_guess[index] == secret_word[index]:
            emojis += green_box  # Both the letter and the position of it are correct
        elif contains_char(secret_word, users_guess[index]):
            emojis += yellow_box  # The letter is right, but its position isn't
        else:
            emojis += white_box  # Incorrect letter, not found in secret word
        index += 1  # Moves loop to next character to check

    return emojis  # Returns the string of emojis that represent the guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turns_taken: int = 1  # The amount of turns that have been used starts at 1
    win: bool = False
    # When win is false, it indicates that the game has not yet ben won
    # Starts as false until the game is won

    while turns_taken <= 6:  # 6 attempts to guess correct secret word
        print(f"=== Turn {turns_taken}/6 ===")
        # Tells user how many turns they have used
        guess: str = input_guess(len(secret))
        # Ask the user for a guess of the correct len based on the secret word's len
        print(emojified(guess, secret))
        # Calls emojified to show the result of the guess with the string of emojis

        if guess == secret:  # Guess and the secret word are exact match
            print(f"You won in {turns_taken}/6 turns!")  # Tells user they won
            win = True  # Win is now set to true to indicate that the game is won
            break  # Because the game is won, the loop is exited
            # It no longer prompts user to input another guess
        turns_taken += 1
        # For every guess made by user, increase number of turns taken by 1
        # Increasing allows for next guess
        # Only increase the turns taken value, if the game has not been won

    if win == False:
        # Only for if the game wasn't won after alloted number of turns
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")  # The secret word of the game is codes!
