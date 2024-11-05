"""Practice with dictionary functions."""

__author__ = "730676761"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values of the input dictionary."""
    inverted_dict: dict[str, str] = {}
    # Create an emtpy dictionary to hold the inverted keys/vals
    for key in input_dict:  # Loop through each key in the input dictionary
        value = input_dict[key]  # Find the value corresponding to the key
        if value in inverted_dict:
            # Checks whether the value already exists in inverted dict
            # If this is the case there will be duplicate keys, so raise KeyError
            raise KeyError("Duplicate key encountered, cannot invert dictionary")
        inverted_dict[value] = key  # Add the inverted key and value to the new dict
    return inverted_dict  # Return the dictionary with the inverted key and values


def favorite_color(color_dict: dict[str, str]) -> str:
    """Find the most popular color in the dictionary of names and fav colors."""
    color_count: dict[str, int] = {}
    # Create an empty dict to count the occurrences of each color

    for person in color_dict:
        # Loop through each color in the input dict to find names and colors
        color = color_dict[person]  # Find the color associated with the person
        if color in color_count:
            color_count[color] += 1  # Increase count by 1 if color is already a key
        else:
            color_count[color] = 1  # Put count to 1 if color is not already in the dict
    most_pop = ""  # Create a variable to track the most popular color
    max_count = 0  # Create a varaible to track the count of the most popular color

    for person in color_dict:  # Loop through every key again to find most popular color
        color = color_dict[person]
        if color_count[color] > max_count:
            # Update most_pop and max_count if the current color has a higher count
            most_pop = color
            max_count = color_count[color]
    return most_pop
    # Return the most popular color, which is color with the highest occurrence count


def count(frequency_list: list[str]) -> dict[str, int]:
    """Counts the occurrences of each item in the given list and returns a dictionary
    where each key is a unique string from the list and each value is the count of that
    string's occurrences."""
    counts: dict[str, int] = {}
    # Create an empty dict to store the counts of the unique elements

    for current_val in frequency_list:
        # Loop through each item in the list to count the occurrences
        if current_val in counts:
            counts[current_val] += 1  # Increase count by 1 if already in counts
        else:
            counts[current_val] = 1  # Set count to 1 for a new element
    return counts  # Return the dictionary that has each elements count


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Groups words by their starting letter."""
    result: dict[str, list[str]] = {}
    # Create an empty dict to categorize words by their first letter

    for word in words_list:
        # Loop through each word in list to group by first letter
        first_letter = word[0].lower()  # Convert first letter to lowercase
        # Ensures that case sensitivity will not impact
        if first_letter in result:
            # Checks whether the first letter is already a key in result
            result[first_letter].append(
                word
            )  # Add word to existing list for the letter
        else:
            result[first_letter] = [word]
            # Start a new list if letter is not already in key
    return result  # Return the completed dict with words grouped by first letter


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates attendance log by adding a student to the specified day's attenance."""
    if day in attendance_log:
        # Check whether the specified day is already a key in attendance log
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
            # Only add students who aren't already recorded for the day
    else:
        attendance_log[day] = [student]
        # If the day is not in the log then create a new entry with the student


# No return key word since the return type is none
