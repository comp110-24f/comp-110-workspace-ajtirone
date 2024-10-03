"""import function concat from concatenation.py"""

__author__ = "730676761"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"
print(concat(x, y))

xs: str = "123"
ys: str = "abc"
(get_coords(xs, ys))
