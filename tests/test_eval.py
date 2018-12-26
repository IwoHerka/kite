import pytest

from hypothesis import given
from hypothesis.strategies import *

from kite import lisp
from kite.symbol import Symbol, T, F, NIL
from kite.env import Environment
from kite.symbol import Symbol as S, String as Str
from kite.list import List as L
from kite.num import Integer as I, Float as Fl, Rational as R

from .util import rationals, floats_

env = None


def setup_function():
    global env
    env = lisp.get_environment()


def test_eval_symbol():
    t = S('t').eval(env)
    assert t != None
    assert str(t) == 't'


def test_eval_cannot_apply_to_symbol():
    with pytest.raises(TypeError):
        L(T, F, NIL).eval(env)


def test_eval_quoted_list():
    l = L(S('quote'), L(T, F, NIL)).eval(env)

    assert type(l) is L
    assert str(l) == '(t () NIL)'


def test_atom():
    assert L(S('atom'), S('t')).eval(env) == T
    assert L(S('atom'), S('f')).eval(env) == T
    assert L(S('atom'), S('nil')).eval(env) == T

    assert L(S('atom'), L(S('quote'), L(S('t')))).eval(env) == F
    assert L(S('atom'), L(S('quote'), L(S('atom')))).eval(env) == F


def test_eq():
    assert L(S('eq'), S('t'), S('t')).eval(env) == T
    assert L(S('eq'), S('t'), S('f')).eval(env) == F
    assert L(S('eq'), S('t'), L(S('quote'), S('f'))).eval(env) == F


def test_car():
    '(car (t f t f f))'

    assert L(S('car'), L(S('quote'), L(S('t'), S('f')))).eval(env) == S('t')

    with pytest.raises(TypeError):
        L(S('car'), L(S('t'), S('f'))).eval(env)


def test_cdr():
    pass


def test_cons():
    assert (
        L(S('cons'), S('t'), L(S('quote'), L(S('t'), S('f')))).eval(env)
    ) == (
        L(S('t'), S('t'), S('f'))
    )


@given(text())
def test_string_evaluates_to_string(val):
    assert Str(val).eval(env) == Str(val)


@given(integers())
def test_integer_evaluates_to_integer(val):
    assert I(val).eval(env) == I(val)


@given(floats_())
def test_integer_evaluates_to_integer(val):
    assert Fl(val).eval(env) == Fl(val)


@given(rationals())
def test_rational_evaluates_to_rational(val):
    assert R(*val).eval(env) == R(*val)
