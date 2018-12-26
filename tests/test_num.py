from fractions import Fraction

from hypothesis import given
from hypothesis.strategies import *

from kite.num import Integer, Float, Rational


@composite
def rationals(draw):
    return draw(integers()), draw(integers(min_value=1))

@composite
def floats_(draw):
    return draw(floats(allow_nan=False, allow_infinity=False))


@given(integers(), floats_())
def test_addition_0(iv, fv):
    t = Fraction(iv) + Fraction(fv)
    assert Integer(iv).add(Float(fv)) == t
    assert Float(fv).add(Integer(iv)) == t


@given(floats_(), rationals())
def test_addition_1(fv, rv):
    t = Fraction(fv) + Fraction(*rv)
    assert Float(fv).add(Rational(*rv)) == t
    assert Rational(*rv).add(Float(fv)) == t


@given(integers(), rationals())
def test_addition_2(iv, rv):
    t = Fraction(iv) + Fraction(*rv)
    assert Integer(iv).add(Rational(*rv)) == t
    assert Rational(*rv).add(Integer(iv)) == t


@given(integers(), floats_(), rationals())
def test_addition_3(iv, fv, rv):
    t = Fraction(iv) + Fraction(fv) + Fraction(*rv)
    assert Rational(*rv).add(Integer(iv), Float(fv)) == t
