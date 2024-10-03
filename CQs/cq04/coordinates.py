"""Use nested while loop to print coordinate pairs of characters"""

__author__ = "730676761"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs):
        y = 0
        while y < len(ys):
            print((xs[i], ys[y]))
            y += 1
        i += 1


if __name__ == "__main__":
    get_coords("12", "34")
