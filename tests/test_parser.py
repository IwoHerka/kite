from kite.symbol import T, F, NIL, Symbol as S, String as Str
from kite.parser import Parser
from kite.list import List as L
from kite.num import Integer as I, Float as Fl, Rational as R


def parse(string):
    return Parser().parse(string)


def test_parser_0():
    assert parse('(atom t)') == L(S('atom'), S('t'))


def test_parser_1():
    assert parse('(atom ())') == L(S('atom'), L())


def test_parser_2():
    assert parse(
        '(atom (quote (t f t)))'
    ) == (
        L(S('atom'), L(S('quote'), L(S('t'), S('f'), S('t'))))
    )


def test_parser_3():
    assert parse(
        '(quote () ((1 2)) (atom (t (t f))))'
    ) == (
        L(S('quote'), L(), L(L(I(1), I(2))), L(S('atom'), L(S('t'), L(S('t'), S('f')))))
    )


def test_parser_4():
    assert parse(
        '((()) (() () ((()))) ())'
    ) == (
        L(L(L()), L(L(), L(), L(L(L()))), L())
    )


def test_parser_5():
    assert parse('()') == L()


def test_parser_6():
    assert parse('t') == S('t')


def test_parser_7():
    assert parse('') == None


def test_parser_8():
    assert parse(
        "(cons t '(t t))"
    ) == (
        L(S('cons'), T, L(S('quote'), L(T, T)))
    )


def test_parser_9():
    assert parse(
        "(cons t '((atom ()) (atom t)))"
    ) == (
        L(S('cons'), T, L(S('quote'), L(L(S('atom'), L()), L(S('atom'), T))))
    )


def test_parser_10():
    assert parse(
        "((()) (() () ((cons () '(() ())))) ())"
    ) == (
        L(L(L()), L(L(), L(), L(L(S('cons'), L(), L(S('quote'), L(F, F))))), L())
    )


def test_parser_11():
    assert parse(
        "'(t '(t '(() () ()) t))"
    ) == (
        L(S('quote'), L(T, L(S('quote'), L(T, L(S('quote'), L(F, F, F)), T))))
    )


def test_parser_12():
    assert parse("""
        "string"
    """) == (
        Str("string")
    )


def test_parser_13():
    assert parse("""
        (cond (f "false") ((atom t) "true"))
    """) == (
        L(S('cond'), L(S('f'), Str("false")), L(L(S('atom'), T), Str('true')))
    )


def test_parser_13():
    assert parse("""
        (cons "1" '("2" "3"))
    """) == (
        L(S('cons'), Str('1'), L(S('quote'), L(Str('2'), Str('3'))))
    )


def test_parser_14():
    assert parse("""
        (+ 1 2)
    """) == (
        L(S('+'), I(1), I(2))
    )
