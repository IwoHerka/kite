from hypothesis import given
from hypothesis.strategies import *


@composite
def anything_except_string(draw):
    return draw(
          builds(object)
        | builds(list)
        | builds(tuple)
        | builds(dict)
        | builds(set)
        | builds(int)
        | builds(float)
    )


@composite
def two_different_names(draw):
    name = draw(text())
    return name, name + '.'


@composite
def rationals(draw):
    return draw(integers()), draw(integers(min_value=1))

@composite
def floats_(draw):
    return draw(floats(allow_nan=False, allow_infinity=False))
