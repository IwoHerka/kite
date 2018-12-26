from fractions import Fraction
import re


class Integer(int):
    pattern = re.compile('^[-+]?[0-9]+$')

    @classmethod
    def matches(cls, val):
        return bool(cls.pattern.match(val))

    def add(self, *args):
        return Fraction(self) + sum(map(lambda x: Fraction(x), args))

    def eval(self, env, args=None):
        return self


class Float(float):
    pattern = re.compile('^[-+]?[0-9]+[.]?[0-9]*[f]?$')

    def add(self, *args):
        return Fraction(self) + sum(map(lambda x: Fraction(x), args))

    @classmethod
    def matches(cls, val):
        return bool(cls.pattern.match(val))

    def eval(self, env, args=None):
        return self

    def _generic_op(self, other, op):
        if isinstance(other, Rational):
            return op(other, Decimal(self))
        else:
            return op(Decimal(self), other)


class Rational(Fraction):
    pattern = re.compile('^[-+]?[0-9]+[/][1-9]+$')

    @classmethod
    def matches(cls, val):
        return bool(cls.pattern.match(val))

    def __str__(self):
        return '{}/{}'.format(
            self.numerator,
            self.denominator
        )

    def __repr__(self):
        return str(self)

    def add(self, *args):
        return Fraction(self) + sum(map(lambda x: Fraction(x), args))

    def eval(self, env, args=None):
        return self
