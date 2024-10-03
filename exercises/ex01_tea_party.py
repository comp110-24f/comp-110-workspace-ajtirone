"""Writing program to plan a tea party"""

__author__: str = "730676761"


def main_planner(guests: int) -> None:
    """Call each function and produce the printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # add space between quotations to output proper formatting
    # originally, with no spaces, for, guests, people concatenated into one word

    print("Tea Bags: " + str(tea_bags(people=guests)))
    # print number of tea bags required
    # add space between : and quotation for proper concatenation spacing
    # convert integer from tea_bags to string to concatenate

    print("Treats: " + str(treats(people=guests)))
    # print number of treats required
    # add space between : and quotation for proper concatenation spacing
    # convert integer from treats to string to concatenate

    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # print the total cost of the tea party
    # find cost with tea_bags and treats
    # convert cost float to string to conacatenate with dollar sign

    return None  # function returns None by default, but adding return for clairty


def tea_bags(people: int) -> int:
    """Compute number of tea bags based on number of guests"""
    return people * 2
    # multiply number of guests by 2, since each guest will drink 2 cups of tea


def treats(people: int) -> int:
    """Compute number of treats based on number of teas guests will drink"""
    return int(tea_bags(people=people) * 1.5)
    # call tea bag function with total number of teas (2 per guest)
    # multiply by 1.5 assuming each tea a guest drinks they want 1.5 treats to accompany
    # make return vlaue integer


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)
    # multiply number of tea bags by 0.50 to find cost per tea bag
    # multiply number of treats by 0.75 to find cost per treat
    # add both costs together to find total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
    # call main planner function
    # ask user how many guests will attend, so that program output can be run
