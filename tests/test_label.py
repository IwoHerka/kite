import pytest

from hypothesis import given
from hypothesis.strategies import *

from archaeopteryx.symbol import Symbol as S, T, F, NIL
from archaeopteryx.fn import label
from archaeopteryx import lisp
from archaeopteryx.list import List


@given(just(lisp.get_environment()), text())
def test_label_correctly_assigns_value_to_name(env, name):
    value = List(
        S('label'),
        S(name),
        List(
            S('quote'),
            List(
                S('t'),
                S('f')
            )
        )
    ).eval(env)

    assert value == env.get(name)
